# Pipeline order (WIP!)
import sys
sys.path.append('sensor-pipeline')
import importlib
import simulate_timeseries
importlib.reload(simulate_timeseries)  # For local debugging
import os

# Init environment
out_dir = 'derivatives'
os.makedirs(out_dir, exist_ok=True)

# Call the simulate_time_series function
df = simulate_timeseries.simulate_timeseries_as_df(10)




