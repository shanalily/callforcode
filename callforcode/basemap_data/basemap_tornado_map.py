import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os
from astropy.convolution import Gaussian2DKernel
import sys
import csv
from scipy.signal import convolve

#print(os.listdir("."))
#textfile
textfile = open("/Users/mallorygaspard/Documents/Call For Code 2018/us_cities_pop.txt", encoding="utf-8")
lines = textfile.read().split(',')

#CSV file
fil = open("/Users/mallorygaspard/Documents/Call For Code 2018/output.csv")
cs = csv.reader(fil, delimiter=",", quotechar="\"")
torn_start_longs = []
torn_start_lats = []
torn_end_longs = []
torn_end_lats = []

#plt.show()
    
    
    
composite_list = [lines[x:x+15] for x in range(0, len(lines),15)]
print (composite_list[2])

#print(composite_list[1][])
print(composite_list[(len(composite_list)-1)])
cities = []
long_lat_tuples = []
latitudes = []
longitudes = []
for i in range (1, len(composite_list)-1):
    lat = composite_list[i][6].strip('"')
    longi = composite_list[i][7].strip('"')
    #print(lat)
    cities.append(composite_list[i][1])
    latitudes.append(float(lat))
    longitudes.append(float(longi))
    long_lat_tuples.append((float(lat),float(longi)))
print (cities[3])        
print (long_lat_tuples[2])

#median income, all races, by geographic regions of US
#major_regions = ['North East', 'Midwest', 'South', 'West' ]
#median_income_by_region = [33658,32200, 30729, 32265]
#region_center_city = ["New York City", "Chicago", "Houston", ]
#region_center_city_lats = [40.7128, 41.8781, 29.7604, 34.0522] 
#region_center_city_longs = [-74.0060, -87.6298, -95.3698, -118.2437]
#region_center_city_coords = [(40.71,-74.0060), (41.8781,-87.6298),(29.7604,-95.3698)]

#parsing txt file 

map_image = Basemap(
        projection='merc',
        llcrnrlon=-130,
        llcrnrlat=25,
        urcrnrlon=-60,
        urcrnrlat=50,
        lat_ts=0,
        resolution='i',
        suppress_ticks=True)

# position in decimal lat/lon
#region_city_center_lats=[40.7128,42.82]
#region_city_enter_lons=[-74.0060,-73.95]
# convert lat and lon to map projection
mx,my=map_image(longitudes,latitudes)

# The NetworkX part
# put map projection coordinates in pos dictionary
G=nx.Graph()
pos={}
#G.add_edge('Northeast','Midwest', 'South')
for i in range (0, len(cities)):
    G.add_node(cities[i])
    pos[cities[i]]=(mx[i],my[i])

# draw
nx.draw_networkx(G,pos,node_size=1,node_color='blue', with_labels = False)

astro = Gaussian2DKernel(50, x_size=400, y_size=400)

first_line = True
for line in cs:
    
    if first_line:
        first_line = False
        continue
    torn_start_longs.append(float(line[10]))
    torn_end_longs.append(float(line[11]))
    torn_start_lats.append(float(line[50]))
    torn_end_lats.append(float(line[3]))
    break
    
grid = [[0 for i in range(500)] for j in range(500)]
lat_dif = torn_end_lats[0] - torn_start_lats[0]
longs_dif = torn_end_longs[0] - torn_start_longs[0]

bin_size_long = longs_dif/450
bin_size_lat = lat_dif/450

slope = 1
current_lat = 24
current_long = 24

if longs_dif < 0:
    slope = -1
    current_lat = 474
    current_long = 24

while current_long != 474:
    grid[current_lat][current_long] = 1
    current_lat += slope
    current_long += 1
    
new_grid = convolve(np.array(astro), np.array(grid))


#plt.show()
# Now draw the map
map_image.drawcountries()
map_image.drawstates()
map_image.bluemarble()
map_image.imshow(new_grid, alpha = 0.25, cmap='jet', interpolation="nearest")
plt.colorbar()
#plt.xlim(-1000,1000) 
#plt.ylim = (-1000,1000)
plt.title("Tornado Path Track")
plt.show()
