"""

This script provides a function to calculate the difference between two points

#haversine formula
c = 2 ⋅ atan2( √a, √(1−a) )
d = R ⋅ c
where 	φ is latitude, λ is longitude, R is earth’s radius
radius = 6,371km

"""

from math import radians, cos, sin, asin, sqrt

# Calculates the distance between two points ([lat1,lon1], [lat2,lon2]) in km
def haversine(lat1,lon1,lat2,lon2):
   R = 6371 #Earth's radius in km
   dLat = radians(lat2 - lat1)
   dLon = radians(lon2 - lon1)
   lat1 = radians(lat1)
   lat2 = radians(lat2)

   a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
   c = 2*asin(sqrt(a))
   
   return R*c

#Example

lon1 = -78.678930
lat1 = 28.673913
lon2 = -78.703485
lat2 = 29.826394

print(haversine(lat1,lon1,lat2,lon2))