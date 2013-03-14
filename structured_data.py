from scipy.io import netcdf
from numpy import size, hstack, vstack, array
from sympy import Matrix
import csv

def struct_data(file_path):
  variable_dim = {}
  all_data = netcdf.netcdf_file(file_path)
  all_dimension = all_data.dimensions
  list_of_variables = all_data.variables.keys()
  lat = all_data.dimensions['lat']
  lon = all_data.dimensions['lon']
  mlev = all_data.dimensions['mlev']
  count = 1

  datawrite = open("data.txt","a")
  writer = csv.writer(datawrite)
  
  for variable in list_of_variables:
    var_dim = len(all_data.variables[variable].dimensions)
    if (var_dim >= 3):
      if(var_dim == 3):
        a = all_data.variables[variable].data
        b = a.mean(0)
        c = Matrix(b.reshape(lat*lon,1))
        print variable, c.shape, count
        writer.writerow(b)
#        if count == 1:
 #           M = c
  #      else:
   #         M = hstack([M,c])
    #    count = count + 1
      if (var_dim == 4):
        for i in range(mlev):
          a = all_data.variables[variable].data[:,i,:,:]
          b = a.mean(0)

          c = Matrix(b.reshape(lat*lon,1))
          print variable, c.shape, count
          writer.writerow(b)
#        if count == 1:
    #      if count == 1:
     #       M = c
      #    else:
       #     M = hstack([M,c])
          count = count + 1

  datawrite.close()
  return M
