from tools.mapping import create_map
import geopandas as gpd


gdf = gpd.read_file('../data/input/address_geocodes.shp')
buffer_gdf = gpd.read_file('../data/processing/buffers.shp')

gdf_int = gpd.read_file('../data/processing/intersects/idx_0_int_tract_pop.shp')
tracts_file = gpd.read_file('../data/input/census/tl_2019_36_tract.shp')
index = 0

point = gdf[gdf.index == index]
buffer = buffer_gdf[buffer_gdf.index == index]

create_map(point, buffer, gdf_int, tracts_file, index)
# might need to adjust path default param in create_map
