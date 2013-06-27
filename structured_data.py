from scipy.io import netcdf
from numpy import size, hstack, vstack, array, median
from sympy import Matrix
import csv

def struct_data(file_path):
  variable_dim = {}
  all_data = netcdf.netcdf_file(file_path)
  all_dimension = all_data.dimensions
  list_of_variables = all_data.variables.keys()
 # lat[25] = 41.968, lat[45] = 4.66
 # lon[34] = 63.75,  lon[55] = 103.125
 # lat = all_data.dimensions['lat']
  #lon = all_data.dimensions['lon']
  lat = len(range(26,49))
  lon = len(range(26,55))
#  mlev = all_data.dimensions['mlev'] #Not required for forcing and xtsurf
  time = all_data.dimensions['time']
  count = 1 
 
#  for variable in list_of_variables:
#      var_dim = len(all_data.variables[variable].dimensions)
#      if(var_dim == 3):
#        a = all_data.variables[variable].data
#        b = a.mean(0).reshape(1,lat*lon).ravel()
#        print variable, b.shape, count 
#        count = count + 1
#        writer.writerow(b.tolist())
#      if (var_dim == 4):
#        for i in range(mlev):
#          a = all_data.variables[variable].data[:,i,:,:]
#          b = a.mean(0).reshape(1,lat*lon).ravel()
#          print variable, b.shape, count
#          count = count + 1
#          writer.writerow(b.tolist())

  for variable in list_of_variables:
      
      datawrite = open(variable + ".csv","w")
      writer = csv.writer(datawrite)
      a = all_data.variables[variable].data
      var_dim = len(all_data.variables[variable].dimensions)
      dim =  list(all_data.variables[variable].dimensions)
      count_lat = dim.count('lat')
      if (count_lat !=0):
        for i in range(122):
          if(var_dim == 3):
            b = a[i,25:45,34:55].reshape(1, lat*lon).ravel()
          if (var_dim == 4):
            b = median(a[i,:,25:45,34:55],axis=0).reshape(1, lat*lon).ravel()
          print variable, b.shape, count 
          count = count + 1
          writer.writerow(b.tolist())

#        for i in range(mlev):
#          a = all_data.variables[variable].data[:,i,:,:]
#          b = a.mean(0).reshape(1,lat*lon).ravel()
#          print variable, b.shape, count
#          count = count + 1
 #         writer.writerow(b.tolist())
      else:
        writer.writerow([variable, dim, var_dim])
      datawrite.close()
