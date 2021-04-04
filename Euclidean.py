import math 

def euclidean(x1,y1,x2,y2) :
    xr = x1-x2
    yr = y1-y2
    result = math.sqrt((xr**2) + (yr**2))
    return result

def getDistanceEarth(x1,y1,x2,y2) :
    euclideanResult = euclidean(x1,y1,x2,y2)
    return (euclideanResult * 111.319)
    

print("Finding Euclidean")
x1 = -7.275515
y1 = 112.794895
x2 = -7.276207
y2 =  112.790843
distance = getDistanceEarth (x1, y1, x2, y2)
print (distance , "km") 
# 0.457595134 Km
