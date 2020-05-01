import geopandas as gpd


def get_state_ids(
        geodataframe_points,
        states_geojson='data/input/states.json',
):
    # https://raw.githubusercontent.com/loganpowell/census-geojson/master/GeoJSON/5m/2018/state.json
    geodataframe_states = gpd.read_file(states_geojson)

    points_sj_states = gpd.sjoin(
        geodataframe_points,
        geodataframe_states,
        how='left',
    )  # spatial join to get associate state ids with address points

    return points_sj_states
