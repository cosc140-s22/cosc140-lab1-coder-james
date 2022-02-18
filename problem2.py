#
# Name: Florence
# Collaborator(s): Rachel, James
#

import math

lat1 = math.radians(float(input("what is the latitude for location 1?")))
lon1 = math.radians(float(input("what is the longitude for location 1?")))
lat2 = math.radians(float(input("what is the latitude for location 2?")))
lon2 = math.radians(float(input("what is the longitude for location 2?")))

dlon = lon2 - lon1
dlat = lat2 - lat1
x = (math.sin(dlat/2))**2 + math.cos(lat1)*math.cos(lat2)*(math.sin(dlon/2))**2
y= 2*math.atan2(math.sqrt(x), math.sqrt(1-x))
z = 3956 *y

print ("The distance between the two locations is" + str(z) +"miles.")