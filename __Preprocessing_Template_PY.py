# Imports 
import sys
sys.path.append("/glade/u/home/joyceyang/Joyce_Modules/")
import importlib
import preprocessing
importlib.reload(preprocessing)
from preprocessing import *

year = 2015 

# TSA
h0filenames, h2filenames = filename_generator(year, year) 
output_names = output_name(year, year, prefix='TSA_') #change
for i in range(len(output_names)):
    h0file = h0filenames[i] 
    h2file = h2filenames[i] 
    print('h0file:', h0file)
    print('h2file:', h2file)
    dataDIR = '/glade/scratch/joyceyang/Batch_Jobs/' + output_names[i] + '.nc'
    print(dataDIR) 
    nc = open_file_TSA(h0file, h2file, dataDIR) #change

# RH2M
output_names = output_name(year, year, prefix='RH2M_') #change
for i in range(len(output_names)):
    h0file = h0filenames[i] 
    h2file = h2filenames[i] 
    dataDIR = '/glade/scratch/joyceyang/Batch_Jobs/' + output_names[i] + '.nc'
    print(dataDIR) 
    nc = open_file_RH2M(h0file, h2file, dataDIR) #change

# TREFMXAV
output_names = output_name(year, year, prefix='TREFMXAV_') #change
for i in range(len(output_names)):
    h0file = h0filenames[i] 
    h2file = h2filenames[i] 
    dataDIR = '/glade/scratch/joyceyang/Batch_Jobs/' + output_names[i] + '.nc'
    print(dataDIR) 
    nc = open_file_TREFMXAV(h0file, h2file, dataDIR) #change

# TREFMNAV
output_names = output_name(year, year, prefix='TREFMNAV_') #change
for i in range(len(output_names)):
    h0file = h0filenames[i] 
    h2file = h2filenames[i] 
    dataDIR = '/glade/scratch/joyceyang/Batch_Jobs/' + output_names[i] + '.nc'
    print(dataDIR) 
    nc = open_file_TREFMNAV(h0file, h2file, dataDIR) #change
