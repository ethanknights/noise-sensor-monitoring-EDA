import pandas as pd
import numpy as np
import sys
import datetime

# Read
rawD = pd.read_csv('./data/raw_April2023.csv')
df = rawD.sort_values('Received Date')
del rawD

unique_values_dict = {}
for col in df.columns:
    unique_values_dict[col] = df[col].unique()
    # print("Unique values in column {}: {}".format(col, unique_values))
# sys.getsizeof(unique_values_dict)

print(unique_values_dict['Complaint Type Code'])
print(unique_values_dict['Complaint Type'])
print(unique_values_dict['Complaint Sub Type'])
print(unique_values_dict['AddressKey'][0:9])


tmp = df[df['Complaint Type'] == 'Building Site']
tmp = tmp.sort_values('Received Date')

# add regexp with 2022
tmp = tmp[tmp['Received Date'][7:] == '2022']
# len(tmp)