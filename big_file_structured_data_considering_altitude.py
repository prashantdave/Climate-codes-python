from scipy.io import netcdf
from numpy import size, hstack, vstack, array, median, reshape
from sympy import Matrix
from Scientific.IO.NetCDF import NetCDFFile
import csv

def struct_data(file_path):
  variable_dim = {}
  all_data = NetCDFFile(file_path,'r')
  all_dimension = all_data.dimensions
  list_of_variables = all_data.variables.keys()
 # lat[25] = 41.968, lat[45] = 4.66
 # lon[34] = 63.75,  lon[55] = 103.125
 # lat = all_data.dimensions['lat']
  #lon = all_data.dimensions['lon']
  lat = len(range(26,49))
  lon = len(range(26,55))
#  hlev = range(16)
#  mlev = all_data.dimensions['mlev']
  #ilev = all_data.dimensions['ilev'] #for forcing files as it does not contain mlev
#  time = all_data.dimensions['time']
  #time = 122 # for JJAS
#  time = 92 #for MAM 
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
      a = all_data.variables[variable]
      a = a.getValue().mean(0)
      var_dim = len(all_data.variables[variable].dimensions)
      dim =  list(all_data.variables[variable].dimensions)
      count_lat = dim.count('lat')
      if (count_lat !=0):
        if(var_dim == 3):
#          a = a.mean(0)   
          b = a[26:49,26:55].reshape(1, lat*lon).ravel()
#            b = a[i,26:46,34:55]
 #           datatolist = b.tolist();
  #          datatolist.reverse();
   #         b = array(datatolist);
    #        print b.shape
     #       b = b.reshape(1,lat*lon).ravel()
          writer.writerow(b.tolist())
        
        if (var_dim == 4):          
          hlev = range(a.shape[0])
          b=[]
          for i in hlev:
            b = a[i,26:49,26:55].reshape(1, lat*lon).ravel()
#            b = median(a[i,:,26:46,34:55],axis=0)
 #           datatolist = b.tolist();
  #          datatolist.reverse();
   #         b = array(datatolist);
    #        b = reshape(b,1,lat*lon).ravel()
            writer.writerow(b.tolist())
        print variable, b.shape, count 
        count = count + 1

#        for i in range(mlev):
#          a = all_data.variables[variable].data[:,i,:,:]
#          b = a.mean(0).reshape(1,lat*lon).ravel()
#          print variable, b.shape, count
#          count = count + 1
 #         writer.writerow(b.tolist())
      else:
        writer.writerow([variable, dim, var_dim])
      datawrite.close()
