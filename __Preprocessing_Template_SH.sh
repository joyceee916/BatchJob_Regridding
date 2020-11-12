#! /bin/tcsh
#PBS -N _2015_Preprocessing
#PBS -A UIUC0026
#PBS -j oe
#PBS -l walltime=12:00:00
#PBS -q economy
#PBS -l select=1:ncpus=1:mpiprocs=36
#PBS -m abe
#PBS -M joycey2@illinois.edu

module load python
module load ncarenv
ncar_pylib   

python _2015_Preprocessing.py

