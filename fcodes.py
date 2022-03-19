import json
import pandas as pd
df = pd.read_csv('sz_corpus.csv')

from geopy.geocoders import GeoNames
geo = GeoNames(username='alina3')
admin_list = []
for x in df.lemma:
    print(x)
    try:
        location = geo.geocode(x)
        admin_lvl = location.raw
        admin_list.append(admin_lvl['fcode'])
    except:
        admin_list.append(None)
df['fcode'] = admin_list
df.to_csv("sz_fig.csv")
