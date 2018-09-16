import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap
# from geopy.geocoders import Nominatim
import os
import psycopg2
# from config import config

#print(os.listdir("."))
print ("Volunteer Network Visualizer") 

red_cross_office_option = input("Show Red Cross Offices: Y or N?")

textfile = open(os.path.dirname(os.path.realpath(__file__)) + "/us_cities_pop.txt")
# textfile = open("/Users/mallorygaspard/Documents/Call For Code 2018/us_cities_pop.txt", encoding="utf-8")
lines = textfile.read().split(',')

composite_list = [lines[x:x+15] for x in range(0, len(lines),15)]

#print(composite_list[1][])
cities = []
states = []
long_lat_tuples = []
latitudes = []
longitudes = []
for i in range (1, len(composite_list)-1):
    states.append(composite_list[2])
    lat = composite_list[i][6].strip('"')
    longi = composite_list[i][7].strip('"')
    #print(lat)
    cities.append(composite_list[i][1])
    latitudes.append(float(lat))
    longitudes.append(float(longi))
    long_lat_tuples.append((float(lat),float(longi)))

#median income, all races, by geographic regions of US
#major_regions = ['North East', 'Midwest', 'South', 'West' ]
#median_income_by_region = [33658,32200, 30729, 32265]
#region_center_city = ["New York City", "Chicago", "Houston", ]
#region_center_city_lats = [40.7128, 41.8781, 29.7604, 34.0522] 
#region_center_city_longs = [-74.0060, -87.6298, -95.3698, -118.2437]
#region_center_city_coords = [(40.71,-74.0060), (41.8781,-87.6298),(29.7604,-95.3698)]

#adding in Fema Regional Contacts
fema_regional_contact_offices = ["Denver", "Boston", "New York", "Atlanta", "Chicago", "Kansas City", "Denton", "Oakland", "Seattle"]
fema_lats =[39.7392, 42.3601, 40.7128,33.7490, 41.8781, 39.0997,33.2148, 37.8044, 47.6062]
fema_longs = [-104.9903, -71.0589, -74.0060, -84.3880, -87.6298, -94.5786, -97.1331, -122.2711, -122.3321]

'''for i in range (0, len(cities)):
    if cities[i] == '"Denver"' and states[i] == '"CO"':
        fema_lats.append(latitudes[i])
        fema_lats.append(longitudes[i])
        fema_regional_contact_offices.append(cities[i])'''
               

#adding in american red cross offices 
arc_offices = ["Washington DC", "Montgomery", "Phoenix, AZ", "Albuquerque, NM", "Tuscon,AZ", "Flagstaff, AZ",
"El Paso, TX", "Huntsville, AL", "Opelika, AL", "Tuscaloosa, AL", "Mobile, AL", "Birmingham, AL",
"LIttle Rock, AR", "El Dorado, AR", "Pine Bluff, AR", "Rogers, AR", "Jonesboro, AR", "Fort Smith, AR", "Hot Springs, AR", "Blytheville, AR",
"Bakersfield, California", "Camarillo, California", "Santa Barbara, California", "Fresno, California",
"Stockton, California", "Modesto, California", "Sonora, California", "Turlock, California",
"Santa Ana, California", "Riverside, California", "Rancho Cucamonga, California", "Palm Desert, California",
"San Fransisco, California", "Santa Rosa, California", " Carmel, California", "San Jose, California",
"San Diego, California", "El Centro, California",
"Torrance, California", "Long Beach, California", "Woodland Hills, California", "Pomona, California", "Pasadena, California",
"Denver, Colorado", "Colorado Springs, Colorado", "Grand Junction, Colorado", "Loveland, Colorado",
"Farmington, CT", "Norwich, CT",
"Baltimore, Maryland", "Annapolis, Maryland", "Hagerston, Maryland", "Wilmington, Deleware", "Bethesda, Maryland",
"Winter Haven, Florida", "Orlando, Florida", "Daytona Beach, Florida", "Tampa, Florida", "Sarasota, Florida",
"Tallahassee, Florida", "Jacksonville, Florida", "Pensacola, Florida",
"West Palm Beach, Florida", "Fort Lauderdale, Florida", "Vero Beach, Florida", "Ft. Meyers, Florida", "Vero Beach, Florida",
"Atlanta, Georgia", "Watkinsville, Georgia", "Savannah, Georgia", "Fort Gordon, Georgia", "Fort Stewart, Georgia",
"Americus, Georgia", "Rome, Georgia", "Augusta, Georgia", "LaGrange, Georgia",
"Valdosta, Georgia", "Columbus, Georgia",
"Bosie, Idaho", "Idaho Falls, Idaho",
"Chicago, IL", "Rockford, Illinois", "Romeoville, Illinois",
"Peoria, Illinois", "Springfield, Illinois", "Moline, Illinois",
"Indianapolis, Indiana", "Evansville, Indiana", "Terre Haute, Indiana",
"South Bend, Indiana", "Indianapolis, Indiana", "Fort Wayne, Indiana",
"Merrillville, Indiana", "Des Moines, Iowa", "Cedar Rapids, Iowa", "Dubuque, Iowa", "Sioux City, Iowa",
"Topeka, Kansas", "Salin, Kansas", "Wichita, Kansas",
"Baton Rouge, Louisiana", "Shreveport, Louisiana", "New Orleans, Louisiana",
"Topsham, Maine", "Bangor, Maine", "Caribou, Maine", "Lewiston, Maine",
"Hyannis, MA", "Worcester, MA", "Peabody, MA", "Springfield, MA", "Medford, MA",
"Warren, Michigan", "Ann Arbor, Michigan", "Riverview, Michigan", "Flint, Michigan",
"Bloomfield, Michigan", "Lansing, Michigan", "Livonia, Michigan", "Farmington Hills, Michigan",
"Muskegon, Michigan", "Minneapolis, MN", "Duluth, MN", "Rochester, Minnesota", "St. Cloud, Minnesota",
"Mankato, Minnesota", "Tupelo, Mississippi", "Gulfport, Mississippi", "Flowood, Mississippi",
"St. Louis, Missouri", "Kansas City, Missouri", "Columbia, Missouri", "Springfield, Missouri",
"Cape Girardeau, Missouri", "Ft. Leonard Wood, Missouri",
"Lincoln, Nebraska", "Grand Island, Nebraska", "Omaha, Nebraska",
"Las Vegas, Nevada", "Reno, Nevada",
"Concord, New Hampshire", "Burlington, Vermont",
"Fairfield, New Jersey", "Ocean, New Jersey", "Princeton, New Jersey",
"Pleasantville, New Jersey", "Pennsauken, New Jersey", "Summit, New Jersey",
"Poughkeepsie, New York", "Utica, New York", "Morrisonville, New York",
"Albany, New York", "Fort Drum New York",
"New York, New York", "Mineola, New York", "Greenwich, Connecticut",
"Syracuse, New York", "Corning, New York", "Rochester, New York", "Endicott, New York",
"Buffalo, New York",
"Wilmington, North Carolina", "Durham, North Carolina", "Greenville, North Carolina",
"Fayetteville, North Carolina", "Raleigh, North Carolina", "Camp LeJeune, North Carolina", 
"Greenville, North Carolina", "Charlotte, North Carolina", "Hickory, North Carolina",
"Asheville, North Carolina", "Greensboro, North Carolina", "Rock Hill, South Carolina",
"Fargo, North Dakota", "Minot, North Dakota", "Sioux Falls, South Dakota", "Rapid City, South Dakota",
"Bismark, North Dakota", "Columbus, Ohio", "Newark, Ohio", "Findlay, Ohio", "Norwhich, Ohio", 
"Lima, Ohio", "Toledo, Ohio", "Cincinnati, Ohio", "Springfield, Ohio",
"Portsmouth, Ohio", "Greenville, Ohio", "Troy, Ohio", "Dayton, Ohio",
"Cleveland, Ohio", "Wooster, Ohio", "Youngstown, Ohio", "Canton, Ohio",
"Akron, Ohio", "Oklahoma City, Oklahoma", "Shawnee, Oklahoma", "Stillwater, Oklahoma",
"Tulsa, Oklahoma", "Bend, Oregon", "Vancouver, Washington", "Eugene, Oregon", "Portland, Oregon",
"Philadelphia, Pennsylvania", "Allentown, Pennsylvania", "Reading, Pennsylvania", "Stroudsburg, Pennsylvania",
"Wilkes-Barre, Pennsylvania", "Pittsburgh, Pennsylvania", "Oil City, Pennsylvania", "Johnstown, Pennsylvania",
"Lewisburg, Pennsylvania", "Greensburg, Pennsylvania", "York, Pennsylvania", "Erie, Pennsylvania",
"Harrisburg, Pennsylvania", "State College, Pennsylvania",
"Providence, Rhode Island", "North Charleston, South Carolina", "Columbia, South Carolina",
"Greenville, South Carolina", "Myrtle Beach, South Carolina", "Murfreesboro, Tennesse",
"Nashville, TN", "Johnson City, TN", "Clarksville, TN", 
"Austin, Texas", "Woodway, Texas", "Kerrville, Texas", "Midland, Texas", "San Antonio, Texas",
"Dallas, Texas", "Tyler, Texas", "Denison, Texas", "Lubbock, Texas", "Texarkana, Texas", "Abilene, Texas",
"Amarillo, Texas", "Corpus Christi, Texas", "Harlingen, Texas",
"Houston, Texas", "Orange,Texas", "Layton, Utah", "Orem, Utah",
"Salt Lake City, Utah", "Saint George, Utah",
"Richmond, Virginia", "Fort Belvoir, Virginia", "Portsmouth, Virginia",
"Seattle, Washington", "Kennewick, Washington", "Spokane, Washington",
"Bellingham, Washington", "Tacoma, Washington", "Bremerton, Washington",
"Everett, Washington", "Charelston, West Virginia",
"Wausau, Wisconson", "Oshkosh, Wisconson", "Spooner Avenue, Wisconson",
"Milwaukee, Wisconson", "Madison, Wisconson", "Cheyenne, Wyoming"]
arc_lats = [38.9072]
arc_longs = [-77.0369]


#fema graph 
'''Femag = nx.Graph()
pos= {}
for i in range (0, len(fema_lats)):
    Femag.add_node(fema_regional_contact_offices[i])
    pos[fema_regional_contact_offices[i]]=(fema_x[i],fema_y[i])
nx.draw_networkx(Femag,pos,node_size=100,node_color='green', with_labels = False)'''

#ARC Graph
if red_cross_office_option == "Y" or "y":
    
    
    map_image = Basemap(
        projection='merc',
        llcrnrlon=-130,
        llcrnrlat=25,
        urcrnrlon=-60,
        urcrnrlat=50,
        lat_ts=0,
        resolution='i',
        suppress_ticks=True)
    
    geolocator = Nominatim()
    Redcross = nx.Graph()
    pos = {}
    for city in arc_offices:
        try:
            loc = geolocator.geocode(city)
            arc_x, arc_y = map_image(loc.longitude, loc.latitude)
            Redcross.add_node(city)
            pos[city]=(arc_x,arc_y)
            nx.draw_networkx(Redcross,pos,node_size=100,node_color='red', with_labels = False)
        except:
            continue
     

    # position in decimal lat/lon
    #region_city_center_lats=[40.7128,42.82]
    #region_city_enter_lons=[-74.0060,-73.95]
    # convert lat and lon to map projection
    mx,my=map_image(longitudes,latitudes)
    fema_x, fema_y = map_image(fema_longs, fema_lats)
    # The NetworkX part
    # put map projection coordinates in pos dictionary
    G=nx.Graph()
    pos={}
    #G.add_edge('Northeast','Midwest', 'South')
    for i in range (0, len(cities)):
        G.add_node(cities[i])
        pos[cities[i]]=(mx[i],my[i])
    nx.draw_networkx(G,pos,node_size=1,node_color='blue', with_labels = False)       
    # Now draw the map
    map_image.drawcountries()
    map_image.drawstates()
    map_image.bluemarble()
    plt.title("US Mainland Population Density and American Red Cross Offices")
    plt.show()
    
else:
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
    fema_x, fema_y = map_image(fema_longs, fema_lats)
    # The NetworkX part
    # put map projection coordinates in pos dictionary
    G=nx.Graph()
    pos={}
    #G.add_edge('Northeast','Midwest', 'South')
    for i in range (0, len(cities)):
        G.add_node(cities[i])
        pos[cities[i]]=(mx[i],my[i])
    nx.draw_networkx(G,pos,node_size=1,node_color='blue', with_labels = False)       
    # Now draw the map
    map_image.drawcountries()
    map_image.drawstates()
    map_image.bluemarble()
    plt.title("US Mainland Population Density")
    plt.show() 