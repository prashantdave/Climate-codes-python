from scipy.io import netcdf
from numpy import size, hstack, vstack, array
from sympy import Matrix
import csv

def matrix_generator(file_path):
 data_dimension=(1,128,256)
 no_of_grid_points = 1
 gp_to_be_picked = 16
 data_with_same_dimension = {}
 all_data = netcdf.netcdf_file(file_path)
 list_of_variables = all_data.variables.keys()
 no_of_grid_points = array(data_dimension).prod() 
 
 for variable in list_of_variables:
     if (data_dimension == all_data.variables[variable].shape):
         data_with_same_dimension.update({i:all_data.variables[variable][:]})
 
 i = 0
 stacked_data=[]
 for i in range(data_dimension[1]): 
     j = 0
     while (j < (data_dimension[2])):
         for variable in data_with_same_dimension.keys():
             temp = data_with_same_dimension[variable]
             stacked_data = hstack([stacked_data,temp[0][i][j:j+gp_to_be_picked]])
         j = j + gp_to_be_picked
 
 datafile = open("data.txt",'a')
 writer = csv.writer(datafile)
 writer.writerow(stacked_data)
 datafile.close()
 
 return stacked_data
