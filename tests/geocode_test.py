import pandas as pd
from tools.geocode import geocode_dataframe

df = pd.read_csv('../data/input/address_test.csv')

gdf = geocode_dataframe(df, 'address')

print(gdf)
