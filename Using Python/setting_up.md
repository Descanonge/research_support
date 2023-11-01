# Setting up Python

This guide will cover how to install python and all the packages you need quickly, anywhere, and reliably!

For a good python install, you need:
1. python itself,
2. a way to install packages and their dependencies,
3. virtual environments.

The third point is optional, but recommended. That way you avoid incompatibilities between packages, and if you play around too much and break your install you can always just start your environment over.
It can also help dealing with multiple projects at the same time.

This guide will focus on a single tool that achieves all three points.
See the end of the guide for alternatives.

## Micromamba

### Micromamba - Mamba - Conda ?

Let's clarify the toponymy first.

Anaconda is a company that developed the tool we are interested in: [conda](https://docs.conda.io/en/latest/).
This tool allows you to manage virtual environments and packages (not only python, other software as well).
Anaconda also designate a distribution of python, with plenty of common scientific packages and software (Numpy, Jupyter, Spyder for instance).
Because this is a lot to download, an installer is available without any packages: [miniconda](https://docs.conda.io/projects/miniconda/en/latest/), you choose what you want to install.

The community has improved upon those tools. Packages are build automatically by the community and uploaded onto a specific 'channel' of Anaconda: [conda-forge](https://conda-forge.org/). It is recommended to use this channel over Anaconda's defaults. See the [miniforge](https://github.com/conda-forge/miniforge#download) installer which automatically configure conda that way.

The executable tool itself has been rewritten to be faster: this is [mamba](https://github.com/mamba-org/mamba).
However, as for all previous tools, it still needs a base python install. This is why the installers come with a base python install at a specific version. It's a bit heavier to download and make it more difficult to change version.
To counter this we can use [micromamba](https://mamba.readthedocs.io/en/latest/micromamba-installation.html).
It combines everything: it is very light and easy to install, fast, and well documented.

### Setting up

We only need to run this command and follow the instructions:
``` shell
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
```
(check the [documentation](https://mamba.readthedocs.io/en/latest/micromamba-installation.html) for details on a windows install)

The command above will create a folder (`~/micromamba` by default) where all the packages will be placed.
It will also add some code to your `~/.bashrc` to hook micromamba to your shell.
Either run `source ~/.bashrc` or restart your terminal so that it takes effect.

It's best to configure micromamba to always use the conda-forge channels.
We just need to create `~/.mambarc`:
``` yaml
channels:
    - conda-forge
    - defaults
always_yes: true  # optional, just to be faster
```
You can also add this to your `~/.bashrc` if you think the mamba banner is a bit much:
``` shell
export MAMBA_NO_BANNER='yes'
```

You can now use any conda command you might already now (and then some!).

Again, it is recommended to have a virtual environment for each project (at the very least do not install directly in the base environment).
Let's setup an example project. For that we will create a file `env.yml` specifying the software we need.
``` yaml
name: myproject
dependencies:
    # We start with python, specifying the version we want.
    # The version just before the latest version is generally
    # a good and safe choice
    - python=3.10
    
    # let's add some common packages
    - ipython
    - numpy
    - scipy
    - matplotlib
    
    # it's even better to specify the version
    # that way, our work is more easily reproducible
    - xarray=2023.11.*
    - netCDF4=1.6.*
    
    # if the package is not available on conda, we can still use pip:
    - pip
    - pip:
        - tol_colors==1.2.*
```
The star means we do not fix the patch version, so we can update and have bug fixes, but no major changes that could break stuff (see [semantic versioning](https://semver.org/)).
For details on the syntax of this file see the [documentation](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html#specification-files).

We can now create our environment with all those packages:
``` shell
micromamba env create -f env.yml
```
It may take a little bit of time to check the repositories and to resolve dependencies such that there is no incompatibilities.
You can now activate the environment, making all software and package available: `micromamba activate myproject`.

To avoid forgetting to activate, you can use [direnv](https://github.com/direnv/direnv) by creating an `.envrc` file in your project root directory:
``` shell
eval "$(micromamba shell hook --shell bash --root-prefix "$MAMBA_ROOT_PREFIX")"
micromamba activate myproject 
```
This will activate automatically when going into the project root directory (or one of its subfolder).

You can also install packages any time by running:
``` shell
micromamba install matplotlib
```
Make sure to run this while the appropriate environment is activated!
If your desired package is available on pip you can do (again with the environment activated):
``` shell
python -m pip install some-package
```
Despite what some may say, it is safe and absolutely possible to use conda and pip at the same time.

## Some alternatives

Outside of conda & cie. there are other options to achieve what we want.
We already mentioned pip which can install any python package.
It might struggle on some packages that rely on compiled code, like numpy for instance.
This is not a problem for conda which can even install non-python software, like nodejs.

Another option is [poetry](https://python-poetry.org/docs/), a more recent kind of alternative to pip.
Both pip and poetry can be faster than conda when installing packages, and result in less optional dependencies (see this [blog post](https://blogs.sap.com/2022/05/08/why-you-should-use-poetry-instead-of-pip-or-conda-for-python-projects/)).
You would still need another tool to manage virtual environment, either conda or [pyenv](https://github.com/pyenv/pyenv).
