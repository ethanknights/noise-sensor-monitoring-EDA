# Purpose: Identify building site address info for top 5(?) sites
# Top 5 definition == highest N registered complaints
# ---

# Imports
import pandas as pd
import warnings
import importlib
import setup
warnings.filterwarnings("ignore", message="iteritems is deprecated")
importlib.reload(setup)  # For local debugging

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
