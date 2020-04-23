from tools.buffer_points import buffer_addresses
import geopandas as gpd


point_gdf = gpd.read_file('data/input/address_geocodes.shp')

buffer_distance = 5000

buffered_pts = buffer_addresses(point_gdf, buffer_distance)

print(buffered_pts.head())

print(buffered_pts['geometry'])
