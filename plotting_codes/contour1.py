from mpl_toolkits.basemap import Basemap, cm
import matplotlib.pyplot as plt
import numpy as np
from numpy import array
from scipy.io import netcdf
from Scientific.IO.NetCDF import NetCDFFile
# set up orthographic map projection with
# perspective of satellite looking down at 50N, 100W.
# use low resolution coastlines.

#nc = netcdf.netcdf_file('nc_data/T63_WNUD_10Year_200103.01_aerom.nc')
#nc = netcdf.netcdf_file('nc_data/ECHAM-HAM/T63_WNUD_9year_200103/T63_WNUD_10Year_200103.01_radm.nc')
#nc = netcdf.netcdf_file('nc_data/ECHAM-HAM/T63_WNUD_9year_200103/T63_WNUD_10Year_200103.01_radm.nc')

nc = NetCDFFile('/home/prashant/Desktop/nc_data/ECHAM-HAM/2001/radm/T63_WNUD_10year_2001_0609.01_radm.nc')
prcpvar = nc.variables['TAU_2D']
#data = prcpvar[1,25:45,34:55]
tau_2d = prcpvar.getValue();
data = tau_2d[0,26:46,34:55];
datatolist= data.tolist();
datatolist.reverse();
data = np.array(datatolist);
latcorners = nc.variables['lat'][:]
loncorners = nc.variables['lon'][:]

fig = plt.figure()
#ax = fig.add_axes([0.1,0.1,0.8,0.8])

map = Basemap(projection='stere',lat_0=20,lon_0=80,\
llcrnrlat=5, urcrnrlat=40,\
llcrnrlon=65,urcrnrlon=100,\
rsphere=6371200, resolution='l')
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines()
map.drawstates(color='k', linewidth=0.9)
map.drawcountries()
#map.fillcontinents(color='coral',lake_color='aqua')
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary()
# draw lat/lon grid lines every 30 degrees.
map.drawmeridians(np.arange(65,100,5))
map.drawparallels(np.arange(5,40,5))
# make up some data on a regular lat/lon grid.
#nlats = 50; nlons = 50; delta = 2.*np.pi/(nlons-1)
#lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
#lons = (delta*np.indices((nlats,nlons))[1,:,:])

ny = data.shape[0]; nx = data.shape[1]
lons,lats = map.makegrid(nx,ny)
x,y=map(lons,lats)
wave = data
# compute native map projection coordinates of lat/lon grid.
#x, y = map(lons*180./np.pi, lats*180./np.pi)
# contour data over the map.
cs = map.contour(x,y,wave,2,linewidths=1.5, cmap=cm.s3pcpn)
cbar = map.colorbar(cs,location='bottom',pad="5%")
cbar.set_label('mm')

plt.title('contour lines over filled continent background')
plt.show();
