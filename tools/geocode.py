from geopy.geocoders import Nominatim
from shapely.geometry import Point
from geopandas import GeoDataFrame


geolocator = Nominatim(user_agent='pratt_geospatial')


def geocode_dataframe(address_dataframe, address_column):
    df = address_dataframe.copy()


    # geocode address column by apply-ing geolocator.geocode
    df['geocode'] = df[address_column].apply(geolocator.geocode)

    # create a geometry column
    df['geometry'] = df['geocode'].apply(
        lambda x:
        Point(x.longitude, x.latitude)
    )

    # create a geodataframe called gdf from df
    # define the .crs =  {'init': 'epsg:4326'}
    gdf = GeoDataFrame(df, geometry='geometry', crs='epsg:4326')

    # drop the geocode column from the gdf
    gdf = gdf.drop(['geocode'], axis=1)

    return gdf
