from geopy.geocoders import Nominatim
from shapely.geometry import Point  # importing the Point class
from geopandas import GeoDataFrame


geolocator = Nominatim(user_agent='pratt_geospatial')


def geocode_dataframe(address_dataframe, address_column):
    df = address_dataframe.copy()
    df['geocode'] = df[address_column].apply(geolocator.geocode)

    df['geometry'] = df['geocode'].apply(
        lambda x: Point(x.longitude, x.latitude)
    )  # create a geometry column

    gdf = GeoDataFrame(
        df,
        geometry='geometry',
    )

    gdf.crs = {'init': 'epsg:4326'}

    return gdf.drop(columns=['geocode'])
