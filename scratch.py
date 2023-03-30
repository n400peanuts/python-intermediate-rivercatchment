import datetime

import pandas as pd
import numpy as np
from catchment.models import Site, Location
import datetime

data = pd.DataFrame(
    [
        [1., 2.2, 3.],
        [4., 5., 6.]
    ],
    index=['fp35', 'fp56']
)

location_measurement = [
    ("FP", "FP35", "Rainfall"),
    ("FP", "FP56", "River Level"),
    ("PL", "PL23", "River Level"),
    ("PL", "PL23", "Water ph")
]

index_names = ["Catchment", "Site", "Measurement"]
index = pd.MultiIndex.from_tuples(location_measurement, names=index_names)

df_ = [
    [1., 2.2, 3.],
    [4., 5., 6.],
    [38., 29, 34.],
    [7., 5.5, 3.]
]

df = pd.DataFrame(df_, index=index)

measurement_data = [
    {
        'Site': 'FP35',
        'Measurement': 'Rainfall',
        'data': [0., 2., 1.]
    },
    {
        'Site': 'FP56',
        'Measurement': 'River Level',
        'data': [4., 5., 6.]
    }
]

def attach_sites(data_array, sites_list, measurement_list):
    out = []
    for data_row, measurement, sites in zip(data_array, sites_list, measurement_list):
        out.append({'Site':sites,
                    'Measurement':measurement,
                    'Data':data_row})
    return out

data_ = np.array([[34., 32., 33.],
                       [7.8, 8.6, 7.9]])

sites_ = ['PL23', 'PL23']
measure = ['River Level', 'ph']

output = attach_sites(data_, sites_, measure)

FP35 = Site(name='FP35')

rainfall_data = pd.Series(
    [34., 32., 33.],
    index=[
        datetime.date(2000,1,1),
        datetime.date(2000,1,2),
        datetime.date(2000,1,3)
    ]
)

water_ph_data = pd.Series(
    [7.8, 4.3, 5.5],
    index=[
        datetime.date(2000,1,1),
        datetime.date(2000,1,2),
        datetime.date(2000,1,3)
    ]
)

FP35.add_measurement('Rainfall', rainfall_data)
FP35.add_measurement('Water ph', water_ph_data)

print(FP35.measurements['Water ph'])

PL12 = Location('PL12')
print(PL12.name)

PL12.add_measurement('Rain', rainfall_data)
#last_data = FP35.last_measurement
#print(last_data)




