# Purpose: Identify building site address info for top 5(?) sites
# Top 5 definition == highest N registered complaints
# ---

# Imports
import os
import pandas as pd
import warnings
import importlib
import setup
importlib.reload(setup)  # For local debugging

# Init environment
os.makedirs('derivatives', exist_ok=True)
warnings.filterwarnings("ignore", message="iteritems is deprecated")

# Read
# rawD = setup.read_data()  # keep persistent copy for reference during development
df = setup.read_data()

# Preprocess datetime columns
df = setup.convert_raw_date_time(df)
df = setup.remove_missing_date_rows(df)
df = setup.create_joined_datetime(df)

# Sort by datetime
df = df.sort_values('Received DateTime')

# Filter to 'Building Site' complaints
df = df[df['Complaint Type'].isin(['Building Site', 'Building site'])]
print('Dropping non-building sites')
setup.describe_data(df)


# Subset for latest 2 months
first_date = '2023-01-28'
last_date = '2023-03-28'
print(f'Getting subset of complaints within these dates (inclusive):\n{first_date} - {last_date}')
df = setup.get_subset_via_dates(df, first_date, last_date)
setup.describe_data(df)
