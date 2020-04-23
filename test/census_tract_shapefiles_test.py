from tools.census_tract_shapefiles import get_census_tracts


for state_id in ['36', '09']:
    print(state_id)
    get_census_tracts(state_id, 'data/input/census')
