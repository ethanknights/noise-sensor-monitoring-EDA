# Purpose: Identify building site address info for top 5(?) sites
# Top 5 definition == highest N registered complaints
# ---

# Imports
import pandas as pd
import importlib
import setup
importlib.reload(setup)   # For local debugging

# Read
df = setup.read_data()  # Could be persistent but data is big: rawD = readData()

# Filter to 'Building Site complaints
df = df[df['Complaint Type'] == 'Building Site']
# df = df.sort_values('Received Date')

# add regexp with 2022
# tmp = tmp[tmp['Received Date'][7:] == '2022']
# len(tmp)
