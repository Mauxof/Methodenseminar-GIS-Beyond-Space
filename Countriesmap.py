import pandas as pd
import geopandas as gpd
import folium
df = pd.read_csv('sz_countries_new.csv')
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
table = world.merge(df, how="left", left_on=['name'], right_on=['country_name'])
table = table.dropna(subset=['fcode'])
countries_map = folium.Map()
folium.Choropleth(
    geo_data=table,
    name='choropleth',
    data=table,
    columns=['country_name', 'loc_frequency'],
    key_on='feature.properties.name',
    fill_color='RdPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Häufigkeit länderspezifischer Lemmata - SZ Korpus'
).add_to(countries_map)
countries_map.save('sz_countries.html')
