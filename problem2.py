#
# Name: James Cavallo
# Collaborator(s):
#
import math


def main():
    long1 =  math.radians(float(input("Longitude of location one? ")))
    lat1 = math.radians(float(input("Latitude of location one? ")))

    long2 = math.radians(float(input("Longitude of location two? ")))
    lat2 = math.radians(float(input("Latitude of location two? ")))

    dlon = long2 - long1
    dlat = lat2 - lat1

    a = (math.sin(dlat / 2))**2 + (math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2) **2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = 3956 * c

    print("Distance: " + str(d))
    




if __name__ == '__main__':
    main()