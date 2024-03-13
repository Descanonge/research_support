"""Download Data from CMEMS using Copernicus Marine Toolbox.

Allows to downloat a subset into multiple files, split by dates. It adds new command
line arguments, the main one being --frequency. It also allows some more customization
of '--output-directory' and '--output-filename'.

Execute this script for more help `python subset_multifile.py --help`.

Requires pandas, but copernicusmarine depends on Xarray which depends on pandas itself.

Concerning implementation:
The Copernicus marine command line tool relies on a python API using the click package.
Extending an existing click command (here subset) is not really intended as far as I
understand, but possible by modifying the command itself. That way we already have
all the options defined.
We replace the callback function by our own, and add/modify parameters as needed.
"""

import logging
import pathlib
from datetime import timedelta
from os import path

import click
import pandas as pd
from copernicusmarine.command_line_interface.group_subset import (
    subset,
)

ISOFORMAT = "%Y-%m-%d %H:%M:%S"
"""Most precise datetime format acceped by copernicus-marine-client."""

# Some funky things might happens, motu meddles with a global log variable
# TODO: check what it does exactly
log = logging.getLogger(__name__)

# Save the original function
subset_callback = subset.callback


def subset_multifile(
    frequency: str, skip_existing: bool, max_retries: int, **kwargs
) -> list[pathlib.Path]:
    """Download subsets into different files.

    See below for definition of parameters. kwargs are passed to original subset
    function.
    """
    failed_files = []
    output_files = []

    # Replace eventual parameters
    kwargs["output_directory"] = str(kwargs["output_directory"]).format(**kwargs)
    kwargs["output_filename"] = str(kwargs["output_filename"]).format(**kwargs)

    days = pd.date_range(
        start=kwargs["start_datetime"], end=kwargs["end_datetime"], freq=frequency
    )
    days_end = days - timedelta(seconds=1)

    # kwargs for a single day
    day_kw = kwargs.copy()
    for day_start, day_end in zip(days, days_end):
        day_kw["start_datetime"] = day_start
        day_kw["end_datetime"] = day_end

        # Replace date parameters in filename
        day_kw["output_filename"] = day_start.strftime(kwargs["output_filename"])
        outfile = path.join(day_kw["output_directory"], day_kw["output_filename"])

        if outfile in output_files:
            raise RuntimeError(
                f"{outfile} has already been written earlier. "
                "Maybe '--output-filename' is wrong."
            )

        if skip_existing and path.isfile(outfile):
            log.info("File %s already exists. Skipping.", outfile)
            continue

        log.info("Downloading %s", outfile)

        # try a couple of times to download
        error = True
        for _ in range(max_retries):
            try:
                output = subset_callback(**day_kw)
            except Exception as e:
                log.info("", exc_info=e)
                exc = e
            else:
                error = False
                output_files.append(output)
                break

        if error:
            log.warning("Failed to download %s after %d tries", outfile, max_retries)
            log.warning("", exc_info=exc)
            failed_files.append(outfile)

    log.info("Download terminated.")
    if len(failed_files) > 0:
        log.warning("%d files could not be downloaded.", len(failed_files))

    return output_files


new_params = [
    click.Option(
        param_decls=["--frequency", "-F"],
        type=str,
        default="D",
        help="""\
        Frequency at which to group time steps in a single file.

        \b
        See `freq` argument of pandas.date_range() for details
        (https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html#pandas.date_range)
        and https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#period-aliases
        for a list of valid aliases.

        Some examples: `D` for daily, `8D` for every 8 days, `M` for monthly.
        """,
    ),
    click.Option(
        param_decls=["--max-retries"],
        type=click.IntRange(1),
        default=3,
        help=(
            "Number of maximum download tries. Sometimes things can go wrong  "
            "temporarily. To make sure that a file won't be downloaded because of "
            "that, try at most this number of times before passing to the next file."
        ),
    ),
    click.Option(
        param_decls=["--skip-existing"],
        type=bool,
        is_flag=True,
        default=False,
        help=(
            "If present, do not re-download files that already exist on disk. "
            "Otherwise, the behavior from --overwrite-output-data option applies."
        ),
    ),
]

# Insert new params (in first position)
subset.params[0:0] = new_params

# Override existing params
params = {p.name: p for p in subset.params}

p = params["output_directory"]
p.help = (
    "Destination folder for the downloaded files. \nNew in subset-multifile: "
    "The default value is the dataset-id. Other options from the command line "
    "(as 'start_datetime', 'minimum_latitude', etc.) can be included in accolades {}."
)
p.default = "{dataset_id}"

p = params["output_filename"]
p.help = (
    "Path for the download files. As for '--output-directory', other parameters from "
    "the command line can be included in accolades {}. The path can contain "
    "subdirectories. It must contain the date, as formatted for the function "
    "datetime.datetime.str.strftime(). See https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes"
    " for details."
)
p.default = "%Y/%Y-%m-%d.nc"

# Change main command help
subset.short_help = "Download subsets of datasets into multiple files."
subset.epilog = """
    Examples:

    \b
    python subset_multifile.py
    --dataset-id cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i
    --variable thetao
    --start-datetime 2022-01-01T00:00:00 --end-datetime 2022-12-31T23:59:59
    --minimum-longitude -6.17 --maximum-longitude -5.08
    --minimum-latitude 35.75 --maximum-latitude 36.30
    --minimum-depth 0.0 --maximum-depth 5.0
    --frequency M
    --output-filename '%Y/{variable}_%Y-%m.nc'
    """

# Change the function to call
subset.callback = subset_multifile

if __name__ == "__main__":
    subset()
