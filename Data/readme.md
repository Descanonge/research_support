# Fantastic Data and Where to Find Them

Some data can be confusing, there may be many different versions, treatment methods, etc.

Add your find and expertise, either in a section below, or its own document if there is much to say.

## CMEMS

aka Copernicus Marine Environment Monitoring Service aka Copernicus Marine Service.
You'll find all kind of data over there: https://data.marine.copernicus.eu/products

To download it efficiently, you can use the brand new Copernicus Marine Toolbox™.
All the information about it can be found in the (quite extensive) [documentation](https://help.marine.copernicus.eu/en/articles/7949409-copernicus-marine-toolbox-introduction).

Watch out: the latest version is `copernicusmarine`, **not** `copernicus-marine-client`.
Also this has replaced `motu`, goodbye Motu, you will not be missed.

### Some tips

Begin by `copernicusmarine login` and enter your username and password, this will save them in an encrypted file so you don't have to re-enter them each time.

This might be useful: [variables glossary](https://marine.copernicus.eu/glossary)

Watch out for the difference between the **product** and the **dataset**. For instance [here](https://data.marine.copernicus.eu/product/SST_GLO_SST_L4_REP_OBSERVATIONS_010_024/description) the product-id is `SST_GLO_SST_L4_REP_OBSERVATIONS_010_024`. We can spot it in the url, and in the classification section.
This product contains two datasets: `C3S-GLO-SST-L4-REP-OBS-SST` and `ESACCI-GLO-SST-L4-REP-OBS-SST`, you can explore them in the map thing (in 'layers', click the top arrow to show the button).
They are also listed if you go to "Data access" on the left.

### Subset multifiles

You may want to use the subset command (to extract a sub-region, or only certain variables, etc.) but it will concatenate everything in a single Netcdf file (if you are using Netcdf and not Zarr in which case this does not concern you), but you may want to have daily files, or weekly files, or whatever-frequency-files.
I got you: [this script](./copernicusmarine-subset-multifile.py) extend the command to automatically make multiple calls and save the file into whatever path you need them.
*Warning though, it's not thoroughly tested.*

### Mask and flags

You may come across a variable named 'mask' or 'flags' with weird values and more importantly, attributes like `flag_values`, `flag_meanings`, or `flag_masks`.
This is a special way to encode multiple flag variables into one (to save disk space). It is described in the [CF convention](https://cfconventions.org/Data/cf-conventions/cf-conventions-1.11/cf-conventions.html#flags), and you can retrieve the information by using the [cf-xarray](https://cf-xarray.readthedocs.io/en/latest/flags.html) package.

If you want to avoid a full package and understand the encoding, you can always retrieve information with a couple of simple bitwise operations, check out [cf-xarray's code](https://github.com/xarray-contrib/cf-xarray/blob/main/cf_xarray/accessor.py#L2898) for an example (maybe not the most readable).

## Bathymethry

You can find bathymetry data at the [ETOPO](https://www.ncei.noaa.gov/products/etopo-global-relief-model) project (NCEI/NOAA).
It's very high-resolution (highest is 15 arc-second, lowest available is 60 arc-second), available in NetCDF or GeoTiff. It covers ocean bathymetry and land topography.

Some older versions are present on spirit at `/bdd/etopo/`.

## High-res satellite photographs

This is mostly for fun, here are a couple of places where you can find some beautiful images.
But also some tools that can let you explore maybe more useful data.

- On https://earthobservatory.nasa.gov you will find a new image *every day* taken either from a satellite or astronauts in the ISS. It is also accompanied by an explanatory text. You can find the high-resolution versions of those images on https://visibleearth.nasa.gov. And since they have been doing this for decades now this is a huge collections of nice wallpapers 😁.

- The ESA is doing something similar with [Observing the Earth](https://www.esa.int/Applications/Observing_the_Earth). A bit more sparse but be sure to check Sentinel images, the zoom feature they have makes it all the more impressive.

- Here are all the photos taken by astronauts! https://eol.jsc.nasa.gov/SearchPhotos/

- You can explore for yourself the images of the various Sentinel satellites at https://dataspace.copernicus.eu/browser (you might have to create an account).
  Maybe of most interest the true color from Sentinel-2, for some stunning images (its bands have resolutions between 10m and 60m!).
  
- And even more data from the NASA: https://www.earthdata.nasa.gov/learn/find-data. Maybe especially using the [Worldview](https://worldview.earthdata.nasa.gov/).
