#
# Name:
# Collaborator(s):
#
import math

lat1=math.radians(float(input("What is the longitude for loc 1? ")))
lon1=math.radians(float(input("What is the latitude for loc 1? ")))
lat2=math.radians(float(input("What is the longitude for loc 2? ")))
lon2=math.radians(float(input("What is the latitude for loc 2? ")))

dlon = lon2 - lon1
dlat = lat2 - lat1
a = (math.sin(dlat/2))**2+ math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2))**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
d = 3956 * c

print("The distance between the two locations is " + str(d) + " miles.")

