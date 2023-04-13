# Purpose: Identify building site address info for top 5(?) sites
# Top 5 definition == highest N registered complaints
# ---

# Imports
import os
import pandas as pd
import warnings
import importlib
import noise_functions
importlib.reload(noise_functions)  # For local debugging

# Init environment
out_dir = 'derivatives'
os.makedirs(out_dir, exist_ok=True)
# pd.set_option('display.max_columns', None); pd.reset_option('display.max_columns') # Options for local debugging
warnings.filterwarnings("ignore", message="iteritems is deprecated")

# Read
# rawD = setup.read_data()  # keep persistent copy for reference during development
df = noise_functions.read_data()

# Preprocess datetime columns
df = noise_functions.convert_raw_date_time(df)
df = noise_functions.remove_missing_date_rows(df)
df = noise_functions.create_joined_datetime(df)

# Sort by datetime
df = df.sort_values('Received DateTime')

# Filter to 'Building Site' complaints
df = df[df['Complaint Type'].isin(['Building Site', 'Building site'])]
print('Dropped non-building sites')
noise_functions.describe_data(df)


# Subset for latest 2 months
first_date = '2023-01-28'
last_date = '2023-03-28'
df = noise_functions.get_subset_via_dates(df, first_date, last_date)
print(f'Got subset of complaints within these dates (inclusive):\n{first_date} - {last_date}')
noise_functions.describe_data(df)

# ---
# Piecemeal EDA
# ---
unique_values_dict = noise_functions.extra_print_unique_data(df)

unique_counts_dict_reference = noise_functions.count_unique_codes(df, 'Noise Complaint Index', out_dir)  # Reference in Uniform
# unique_counts_dict_address = setup.count_unique_codes(df, 'AddressKey', out_dir)  # Ignore: AddressKey - DWH GUID
unique_counts_dict_ward = noise_functions.count_unique_codes(df, 'WardCode', out_dir)
unique_counts_dict_LSOA = noise_functions.count_unique_codes(df, 'LSOACode', out_dir)
unique_counts_dict_MSOA = noise_functions.count_unique_codes(df, 'MSOACode', out_dir)
unique_counts_dict_OutA = noise_functions.count_unique_codes(df, 'OutputArea', out_dir)
