from numpy import size, hstack, vstack, array, median, reshape, ones
from Scientific.IO.NetCDF import NetCDFFile
from glob import iglob

def netcdf_avg():
    i=0
    count=ones((40,40))
    for filename in iglob('*.nc'):
        f = NetCDFFile(filename)
        variable = f.variables['Optical_Depth_Land_And_Ocean_Mean'] 
        AOD = []
        data = variable.getValue()[95:135,240:280]
        if (i==0):
            data_new = data
        else:
            for j in range(40):
                for k in range(40):
                    if (data_new[j,k]!=-9999 and data[j,k]!=-9999):
                        data_new[j,k] = data_new[j,k] + data[j,k]
                        count[j,k] = count[j,k] + 1 
                        print data_new[i,j], count[i,j]
                    elif (data_new[j,k]==-9999 and data[j,k]!=-9999):
                        data_new[j,k] = data[j,k]
        i=i+1
    for j in range(40):
        for k in range(40):
            data_new[j,k] = data_new[j,k]/count[j,k]
    return data_new
