from scipy.io import netcdf
import numpy as np
def matrix_generator(file_path):
 data_dimension=(1,128,256)
 data_with_same_dimension = {}
 all_data = netCDF.netcdf_file('file_path')
 list_of_variables = all_data.variables.keys()
 for i in list_of_variables:
     if (data_dimension == all_data.variables[i].shape):
         data_with_same_dimension = data_with_same_dimension.upate{i:all_data.variables[i][:]}

 return data_with_same_dimension
