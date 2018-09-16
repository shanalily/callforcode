import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os
from astropy.convolution import Gaussian2DKernel
import sys
import csv
from scipy.signal import convolve
from geopy.geocoders import Nominatim
import itertools

num_disas = int(input("How many recent disasters would you like to show?"))

#print(os.listdir("."))
#textfile
textfile = open("/Users/mallorygaspard/Documents/Call For Code 2018/us_cities_pop.txt", encoding="utf-8")
lines = textfile.read().split(',')

#volunteer CSV
#volfil = open("/Users/mallorygaspard/Documents/Call For Code 2018/users.csv")
#volcs = csv.reader(volfil, delimiter=",", quotechar="\"")
vol_usernames = ['User1', 'User2', 'User3', 'User4', 'User5']
vol_city_state = ["Lafayette, LA", "Mobile, AL", "Troy, NY", "Boston, MA", "Brooklyn, NY"]
vol_emt = ['y', 'n', 'y', 'n', 'n']
vol_truck = ['n', 'y', 'y', 'n', 'y']
vol_car = ['n', 'n', 'y', 'y', 'y']
vol_food = ['y','y','y','y','y']
vol_CPR = ['y','y','y','y','y']
vol_contract = ['n','n','y','n','y']
vol_labor = ['y','y','y','y','y']


#CSV file for tornadoes 
fil = open("/Users/mallorygaspard/Documents/Call For Code 2018/output.csv")
cs = csv.reader(fil, delimiter=",", quotechar="\"")
torn_start_longs = []
torn_start_lats = []
torn_end_longs = []
torn_end_lats = []
torn_cities = []
torn_state = []
torn_deaths = []
torn_injuries = []
torn_label = []
first_line = True
for line in cs:
    
    if first_line:
        first_line = False
        continue
    torn_start_longs.append(float(line[10]))
    torn_end_longs.append(float(line[11]))
    torn_start_lats.append(float(line[50]))
    torn_end_lats.append(float(line[3]))
    torn_cities.append(line[19])
    torn_state.append(line[7])
    if len(torn_end_lats)== num_disas:
        break
    
#print (len(torn_start_lats))    
    
composite_list = [lines[x:x+15] for x in range(0, len(lines),15)]
#print (composite_list[2])

#print(composite_list[1][])
#print(composite_list[(len(composite_list)-1)])
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
#print (cities[3])        
#print (long_lat_tuples[2])

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

#tornado origin plot 
tornG = nx.Graph()
pos = {}
tx,ty = map_image(torn_start_longs, torn_start_lats)
for i in range (0, len(torn_start_longs)):
    tornG.add_node(torn_cities[i])
    pos[torn_cities[i]]=(tx,ty)
nx.draw_networkx(tornG,pos,node_size=100,node_color='red', with_labels = False)

#volunteer network 
volG = nx.Graph()
volEMT = nx.Graph()
pos = {}
geolocator = Nominatim()
for city in vol_city_state:
    try:
        loc = geolocator.geocode(city)
        arc_x, arc_y = map_image(loc.longitude, loc.latitude)
        volG.add_node(city)
        pos[city]=(arc_x,arc_y)
        nx.draw_networkx(volG,pos,node_size=100,node_color='yellow', with_labels = False)
    except:
        continue
'''for i in range (0,len(vol_emt)):
    if vol_emt[i] == 'y':
        try:
            loc2 = geolocator.geocode(vol_city_state[i])
            emt_x, emt_y = map_image(loc2.longitude, loc2.latitude)
            volG.add_node(vol_emt[i])
            pos[vol_emt[i]]=(emt_x,emt_y)
            
            nx.draw_networkx(volEMT,pos,node_size=100,node_color='yellow', with_labels = False)
        except:
            continue '''
#print (volG.nodes())
volG.add_path(volG.nodes())
#volG2 = nx.path_graph(len(vol_city_state)
labels_v = []
for i in range (0, len(vol_emt)):
    labels_v = 'Available Volunteer'
#nx.draw_networkx_labels(volG,pos,node_size=100,node_color='yellow', with_labels = False)     
#adding connections between EMT's
#manual for now
#volG.nodes(data=True)
def complete_graph_from_list(L, create_using=None):
    emtG = nx.empty_graph(len(L),create_using)
    if len(L)>1:
        if emtG.is_directed():
            edges = itertools.permutations(L,2)
        else:
            edges = itertools.combinations(L,2)
        emtG.add_edges_from(edges)
    return emtG

S = complete_graph_from_list(volG.nodes())
cluster_s = nx.average_clustering(S,count_zeros=True) 
nodesvg = volG.nodes() 
#print (cluster_s)
#assigning capacity scores based on criteria they can provide 
#emt = 20, food = 15, truck = 10, car = 5, contractor = 15, labor = 10, cpr = 15 
volunteer_capacity = [60, 50, 90, 45, 70]
nx.set_edge_attributes(S, 'capacity', 50)
vol_flow = nx.maximum_flow(S,nodesvg[0] , nodesvg[4], capacity='capacity')
print('Resource Flow Score:', vol_flow[0])
                                                                                                   
#plt.show()
# Now draw the map
map_image.drawcountries()
map_image.drawstates()
map_image.bluemarble()
#map_image.imshow(new_grid, alpha = 0.25, cmap='jet', interpolation="nearest")
#plt.colorbar()
plt.legend(['City', 'Tornado', 'Available Volunteer'])
plt.title("Recent Disaster Tracker")
plt.show()
