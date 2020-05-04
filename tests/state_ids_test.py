from tools.state_ids import get_state_ids
import geopandas as gpd

geocoded_addresses = gpd.read_file('..data/processing/address_geocodes.shp')

gdf = get_state_ids(geocoded_addresses)

print(gdf['GEOID'].unique())
