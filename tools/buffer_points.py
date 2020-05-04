
def buffer_addresses(point_gdf, buffer_distance):
    # project to 3857
    point_gdf.to_crs(epsg=3857, inplace=True)
    # buffer by buffer distance
    point_gdf['geometry'] = point_gdf.buffer(buffer_distance)

    return point_gdf
