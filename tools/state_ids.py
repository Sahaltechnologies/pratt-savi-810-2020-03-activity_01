import geopandas as gpd


def get_state_ids(
        geodataframe_points,
        states_geojson='data/input/states.json',
):
    # geodataframe_points is already a GeoDataFrame
    # states_gepjson is from: https://raw.githubusercontent.com/loganpowell/census-geojson/master/GeoJSON/5m/2018/state.json


    # read states_geojson file (crs -> epsg:4326)
    states_gdf = gpd.read_file(states_geojson)[['GEOID', 'STUSPS', 'NAME', 'geometry']]

    # matching both gdf's crs just in case
    geodataframe_points.to_crs(states_gdf.crs, inplace=True)

    # spatial join to get associate state ids with address points
    points_sj_states = gpd.sjoin(
        geodataframe_points,
        states_gdf,
        how='left',
        op='intersects',    # within <-opposite-> contains
                            # points are within the states
    )

    pd.read_csv(some_csv)

    return points_sj_states

