import geopandas as gpd


def get_state_ids(
        geodataframe_points,
        states_geojson='data/input/states.json',
):
    # states_gepjson is from:
    # https://raw.githubusercontent.com/loganpowell/census-geojson/master/GeoJSON/5m/2018/state.json


    # read geodataframe_points
    points_gdf = gpd.read_file(geodataframe_points)

    # read states_geojson (crs -> epsg:4326)
    states_gdf = gpd.read_file(states_geojson)[['STATEFP', 'STUSPS', 'NAME', 'geometry']]

    # matching both gdf's crs just in case
    points_gdf.to_crs(states_gdf.crs, inplace=True)

    # spatial join to get associate state ids with address points
    points_sj_states = gpd.sjoin(
        points_gdf,
        states_gdf,
        how='left',
        op='intersects',    # within <-opposite-> contains
                            # points are within the states
    )

    return points_sj_states
