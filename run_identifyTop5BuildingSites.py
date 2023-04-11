# Purpose: Identify building site address info for top 5(?) sites
# Top 5 definition == highest N registered complaints
# ---

# Imports
import pandas as pd
import importlib
import setup
importlib.reload(setup)  # For local debugging

# Read
# rawD = setup.read_data()  # keep persistent copy for reference during development
df = setup.read_data()
df = setup.convert_raw_date_time(df)

# Filter to 'Building Site' complaints
df = df[df['Complaint Type'] == 'Building Site']
# df = df.sort_values('Received Date')


# add regexp with 2022
# tmp = tmp[tmp['Received Date'][7:] == '2022']
# len(tmp)
