import pandas as pd
import geopandas as gpd

from tools.census_population_data import get_population_tract_data_for_state
from tools.mapping import create_map
from tools.geocode import geocode_dataframe
from tools.state_ids import get_state_ids
from tools.buffer_points import buffer_addresses
from tools.census_tract_shapefiles import get_census_tracts


def main(
        address_csv,
        address_column,
        buffer_distance=5000,  # 5 kilometer default, in meters
        state_id_column='GEOID'
):
    df = pd.read_csv(address_csv)

    gdf = geocode_dataframe(df, address_column)

    gdf = get_state_ids(gdf)
    for state_id in gdf[state_id_column].unique():
        get_census_tracts(state_id, 'data/input/census')

    buffer_gdf = buffer_addresses(gdf, buffer_distance)
    buffer_gdf[['address', 'GEOID', 'geometry']].to_file(
        'data/processing/buffers.shp'
    )

    for state_id in gdf[state_id_column].unique():
        tracts_gdf = gpd.read_file(
            f'data/input/census/tl_2019_{state_id}_tract.shp'
        )
        pop_df = get_population_tract_data_for_state(state_id)

        tracts_pop_gdf = pd.merge(
            tracts_gdf,
            pop_df,
            left_on='GEOID',
            right_on='GEOID',
            how='left',
        )

        tracts_pop_gdf.to_crs(epsg=3857, inplace=True)

        tracts_pop_gdf['orig_area'] = tracts_pop_gdf.area

        tracts_pop_gdf.to_file(
            f'data/processing/tl_2019_{state_id}_tract_pop.shp'
        )

    for index, row in buffer_gdf.iterrows():
        tracts_file = gpd.read_file(
            f"data/processing/tl_2019_{row['GEOID']}_tract_pop.shp"
        )

        point = gdf[gdf.index == index]
        buffer = buffer_gdf[buffer_gdf.index == index]

        gdf_int = gpd.overlay(
            buffer,
            tracts_file.to_crs(epsg=3857),
            how='intersection',
        )

        gdf_int['int_area'] = gdf_int .area
        gdf_int['pct_orig_area'] = gdf_int['int_area'] / gdf_int['orig_area']
        gdf_int['pop_est'] = gdf_int['pct_orig_area'] * gdf_int['B01003_001']

        gdf_int.to_file(
            f'data/processing/intersects/idx_{index}_int_tract_pop.shp'
        )

        create_map(point, buffer, gdf_int, tracts_file, index)
        # this is called each time within the loop


if __name__ == '__main__':
    main('data/input/address.csv', 'address')
