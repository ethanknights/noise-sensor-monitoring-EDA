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
out_dir = 'derivatives'
os.makedirs(out_dir, exist_ok=True)
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

# ---
# Piecemeal EDA
# ---
unique_values_dict = setup.extra_print_unique_data(df)

unique_counts_dict_reference = setup.count_unique_codes(df, 'Noise Complaint Index', out_dir)  # Reference in Uniform
# unique_counts_dict_address = setup.count_unique_codes(df, 'AddressKey', out_dir)  # Ignore: AddressKey - DWH GUID
unique_counts_dict_ward = setup.count_unique_codes(df, 'WardCode', out_dir)
unique_counts_dict_LSOA = setup.count_unique_codes(df, 'LSOACode', out_dir)
unique_counts_dict_MSOA = setup.count_unique_codes(df, 'MSOACode', out_dir)
unique_counts_dict_OutA = setup.count_unique_codes(df, 'OutputArea', out_dir)
