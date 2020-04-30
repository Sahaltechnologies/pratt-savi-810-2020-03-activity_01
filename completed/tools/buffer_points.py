

def buffer_addresses(point_gdf, buffer_distance):
    pts = point_gdf.copy()

    pts.to_crs(epsg=3857, inplace=True)

    pts['geometry'] = pts.buffer(buffer_distance)

    return pts
