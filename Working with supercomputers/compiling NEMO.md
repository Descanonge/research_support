### Compiling NEMO4.2 on Irene (TGCC)
Work with `git clone --branch 4.2.0 <https://forge.nemo-ocean.eu/nemo/nemo.git> nemo_4.2.0`
Switch to your working environnement 
```
module switch dfldatadir/gen6035
export MODULEPATH=$MODULEPATH:$GEN6035_ALL_HOME/modules/:$HOME/modules/
PATH=$PATH:$HOME/bin
export PATH
```

Load the corresponding modules
```
module load XIOS/xios-trunk_r2331_intel20.0.0_openmpi4.0.2_rh8
module load flavor/hdf5/parallel hdf5/1.8.20 netcdf-c/4.6.0 netcdf-fortran/4.4.4 gnu
module load 
```

### Compiling NEMO on Jeanzay (IDRIS)

```
module load XIOS/xios-trunk_r2331_intel20.0.0_openmpi4.0.2_rh8

module load hdf5/1.10.5-mpi
module load netcdf/4.7.2-mpi
module load netcdf-fortran/4.5.2-mpi

module load gnu

module load nco/4.8.1
module load ncview/2.1.7
module load subversion/1.9.7

```
