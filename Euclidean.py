# import math
from math import radians, cos, sin, asin, sqrt 

def euclidean(x1,y1,x2,y2) :
    xr = x1-x2
    yr = y1-y2
    result = sqrt((xr**2) + (yr**2))
    return result

def getDistanceEarth2(x1,y1,x2,y2) :
    euclideanResult = euclidean(x1,y1,x2,y2)
    return (euclideanResult * 111.319)

def getDistanceEarth (lat1,long1,lat2,long2) :
    latitude1 = radians(lat1)
    longtitude1 = radians(long1)
    latitude2 = radians(lat2)
    longtitude2 = radians(long2)
    deltaLatitude = latitude2 - latitude1
    deltaLongtitude = longtitude2 - longtitude1
    haversineResult = sin(deltaLatitude / 2)**2 + cos(latitude1) * cos(latitude2) * sin(deltaLongtitude / 2)**2
    haversineResult = 2 * asin(sqrt(haversineResult))
    return haversineResult*6371



print("Finding Euclidean")
x1 = -7.275515
y1 = 112.794895
x2 = -7.276207
y2 =  112.790843
distance = getDistanceEarth2 (x1, y1, x2, y2)
distance2 = getDistanceEarth (x1,y1,x2,y2)
print (distance , "km <-- euclidean")
print (distance2, "km <-- haversine") 

# 0.457595134 Km
