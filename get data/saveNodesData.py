import pandas as pd
from geopy.geocoders import Nominatim
import time
import os
import math

df = pd.read_excel('address.xlsx')
results_df = pd.DataFrame(columns=['id', 'label', 'latitude', 'longitude'])


def get_latlng(id, label, coord = None):
    geolocator = Nominatim(user_agent="my_app")

    if coord:
        location = geolocator.geocode(coord, timeout=10)
    else:
        location = geolocator.geocode("Haute Savoie arrêt de bus " + label, timeout=10)


    if location:
        lat, lng = location.latitude, location.longitude
        print(id, label, lat, lng)
        return pd.Series({'id': id, 'label': label, 'latitude': lat, 'longitude': lng})
    else:
        location = geolocator.geocode("Haute Savoie " + label, timeout=10)
        if location:
            lat, lng = location.latitude, location.longitude
            print(id, label, lat, lng)
            return pd.Series({'id': id, 'label': label, 'latitude': lat, 'longitude': lng})
        else:
            print(id, label, 'not found')
            return pd.Series({'id': id, 'label': label, 'latitude': None, 'longitude': None})


for i, row in df.iterrows():

    id = row['id']
    label = row['label']
    coord = row['coord']

    if isinstance(coord, str) and coord != "":
        result = get_latlng(id, label, coord)
    else:
        result = get_latlng(id, label)


    results_df = results_df.append(result, ignore_index=True)

results_df.to_csv('nodes.csv', index=False)

os.system("python saveEdgesData.py")
