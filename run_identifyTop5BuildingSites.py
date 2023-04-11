# Purpose: Identify building site address info for top 5(?) sites (i.e. highest N registered complaints)
import pandas as pd
from setup import read_data

# Read
df = read_data()  # Could be persistent but data is big: rawD = readData()

# Filter to 'Building Site complaints
df = df[df['Complaint Type'] == 'Building Site']
# df = df.sort_values('Received Date')

# add regexp with 2022
# tmp = tmp[tmp['Received Date'][7:] == '2022']
# len(tmp)
