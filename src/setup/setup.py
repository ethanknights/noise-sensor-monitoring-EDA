import pandas as pd
import numpy as np
import sys
import datetime

# Read
rawD = pd.read_csv('./data/raw_April2023_1997-2023.csv')
df = rawD.sort_values('Received Date')
del rawD  # memory!

# Print unique values to get dataset gist
unique_values_dict = {}
for col in df.columns:
    unique_values_dict[col] = df[col].unique()
# print("\n\n\nUnique values in column {}: {}\n".format(col, unique_values_dict))
# sys.getsizeof(unique_values_dict)
print(unique_values_dict['Complaint Type Code'])
print(unique_values_dict['Complaint Type'])
print(unique_values_dict['Complaint Sub Type'])
print(unique_values_dict['AddressKey'][0:9])

# Analysis scripts next:
print('Next:\npython ../identify_top5BuildingSites.py')
