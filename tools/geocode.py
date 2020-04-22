from geopy.geocoders import Nominatim
from shapely.geometry import Point  # importing the Point class
from geopandas import GeoDataFrame


geolocator = Nominatim(user_agent='pratt_geospatial')


def geocode_dataframe(address_dataframe, address_column):
    df = address_dataframe.copy()

    # geocode address column by apply-ing geolocator.geocode 

    # create a geometry column

    # create a geodataframe called gdf from df

    # define the .crs =  {'init': 'epsg:4326'} 

    # drop the geocode column from the gdf  

    return gdf
