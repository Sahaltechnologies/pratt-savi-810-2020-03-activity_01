# In-Class Coding Activity

https://github.com/pratt-savi-810/pratt-savi-810-2020-03-activity_01/issues

This program should;

1. Take in a `.csv` of addresses.
2. Geocode these addresses. 
3. Find out what states these addresses are in. 
4. Download and unzip those state Census Tract shapefiles
5. Buffer the addresses by a given Buffer distance (2 km)
6. Intersect and perform area-weighted interpolation to estimate population within Buffer distance
7. Sum the population in Buffer
8. Print maps of the geocoded address, tract boundaries and buffers. 

### Output Map Example
![map](https://github.com/pratt-savi-810/pratt-savi-810-2020-03-activity_01/blob/master/maps/_examples/map_0_int_tract_pop.png?raw=true)

Note: This Activity uses Python 3
