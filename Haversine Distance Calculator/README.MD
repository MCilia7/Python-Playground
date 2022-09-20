# Python playground
## Haversine Distance Calculator

The Haversine formula is used to calculate the distance between two points, given their latitude and longitude coordinates. It is not necessarily an ideal method to use for the coordinates on earth as it considers the earth as a 'perfect sphere' without taking into account the ellipsoidal shape of it. 

The program involved learning about using the math module to compute basic mathematical formulas. 

### Haversine formula

a = sin(&#916;lat/2)&sup2; + cos(lat1)*cos(lat2)*sin(&#916;lon/2)&sup2;<br>
c = 2*asin(&Sqrt;a)<br>
d = R ⋅ c 

R is earth’s radius = 6371km