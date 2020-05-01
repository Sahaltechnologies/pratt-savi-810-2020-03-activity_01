from census import Census
import pandas as pd


def get_census_tract_acs_data_for_state(
        api_key,
        acs_field_name,
        state_fips,
):
    c = Census(api_key)
    df = pd.DataFrame(
        c.acs5.state_county_tract(
            acs_field_name,
            state_fips,
            '*',
            '*',
        )
    )
    df['GEOID'] = df['state'].astype(str) + \
        df['county'].astype(str) + \
        df['tract'].astype(str)

    return df


def get_population_tract_data_for_state(state_fips):
    df = get_census_tract_acs_data_for_state(
        "30699f15ab4d04a1e0943715b539d256c9a3ee44",
        'B01003_001E',
        state_fips,
    )
    df.to_csv(f'data/input/census_api/pop_{state_fips}.csv', index=False)
    return df
