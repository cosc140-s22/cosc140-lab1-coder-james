#
# Name: James Cavallo
# Collaborator(s):
#

import requests
import math


def main():
    long2 = ""
    long1 = "" 
    lat1 = ""
    lat2 = ""

    addressOne = input("Address One? ")
    response = requests.get("https://nominatim.openstreetmap.org/search?format=json&q=" + addressOne)
    if response:
        if response.status_code == 200:
            result = response.json()
            lat1 = math.radians(float(result[0]["lat"]))
            long1 = math.radians(float(result[0]["lon"]))
        else:
            print(response.status_code)
            return
    else:
        print("error")
        return
    
    addressTwo = input("Address Two? ")
    response = requests.get("https://nominatim.openstreetmap.org/search?format=json&q=" + addressTwo)
    if response:
        if response.status_code == 200:
            result = response.json()
            lat2 = math.radians(float(result[0]["lat"]))
            long2 = math.radians(float(result[0]["lon"]))
        else:
            print(response.status_code)
            return
    else:
        print("error")
        return

    dlon = long2 - long1
    dlat = lat2 - lat1

    a = (math.sin(dlat / 2))**2 + (math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2) **2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = 3956 * c

    print("Distance: " + str(d))
    



if __name__ == '__main__':
    main()





