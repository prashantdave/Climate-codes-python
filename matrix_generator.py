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
 
 for i in list_of_variables:
     if (data_dimension == all_data.variables[i].shape):
         data_with_same_dimension.update({i:all_data.variables[i][:]})
 
 no_of_grid_points = array(data_dimension).prod() 
 
 final_data = []
 data_dim2 = []
 data_dim3 = []
 dim2 = 0
 stacked_data=[]

 for dim2 in range(data_dimension[1]): 
     dim3 = 0
     while (dim3 < (data_dimension[2])):
         for i in data_with_same_dimension.keys():
             temp = data_with_same_dimension[i]
             stacked_data = hstack([stacked_data,temp[0][dim2][dim3:dim3+gp_to_be_picked]])
         dim3 = dim3 + gp_to_be_picked
 datafile = open("data.txt",'a')
 writer = csv.writer(datafile)
 writer.writerow(stacked_data)
 datafile.close()
 return stacked_data
 

