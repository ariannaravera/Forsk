# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 11:32:23 2019

@author: ashwa
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:22:11 2019

@author: ashwa
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#to import the basemap library gave the direct path to the library
import os
os.environ["PROJ_LIB"]="C:\\Users\\ashwa\\Anaconda3\\Library\\share"
from mpl_toolkits.basemap import Basemap

#plotting data on map
import geopandas as gpd
import shapefile as shp


#reading the csv data and storing it in a variable

city=gpd.read_file("F:\\forsk\\Day4,5\\District_Boundary.shp")

csv=pd.read_csv("F:\\forsk\\Day10\\latlong_raj.csv")

lat=csv['LAT'].values
lon=csv['LONG'].values
population = city['POPULATION'].values
area = city['AREA_SQ_KM'].values
dist=csv['DIST'].values


# 1. Draw the map background
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution='h', 
            lat_0=27.0238, lon_0=74.2179,
            width=1.05E6, height=1.2E6)
m.shadedrelief()
m.drawcoastlines(color='blue',linewidth=3)
m.drawcountries(color='gray',linewidth=3)
m.drawstates(color='gray',linewidth=3)

# 2. scatter city data, with color reflecting population
# and size reflecting area
m.scatter(lat,lon, latlon=True,
          c=population,s=500,
          cmap='YlGnBu_r', alpha=0.5)

# 3. create colorbar and legend
plt.colorbar(label=r'Population')
plt.clim(300000, 4000000)


dict1={}
list1=[]
list2=[]
list3=[]
n=0

for z in lat:
    list1.append(z)
for c in lon:
    list2.append(c)
for b in dist:
    list3.append(b)
    
while(n<33):
    dict1[list1[n]]=list2[n]
    n+=1
i=0
# Map (long, lat) to (x, y) for plotting
for z,c in dict1.items():
    x,y = m(z, c)
    plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y,list3[i], fontsize=12);
    i+=1
          
           
           
           
