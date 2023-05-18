import datetime
import random
import pandas as pd

def simulate_timeseries_as_df(duration):
    """
    Simulates a time series of dB values over a specified duration.

    :param duration: The duration of the time series in seconds.
    :type duration: int
    :return: The generated time series as pandas dataframe, with timestamp and dB value.
    :rtype: list[(str, int)]
    """
    
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(seconds=duration)

    timeseries = []
    while datetime.datetime.now() < end_time:

        random_value = random.random()  # Generate a random value between 0 and 1

        percent_of_tS_in_low_dB_range = 0.92  # e.g., 92% of tS = 30-80 dB range, remaining tS in 81-105dB
        if random_value < percent_of_tS_in_low_dB_range:
            data_point = random.randint(30, 80)
        else:
            # Generate occasional spikes in the 81 to 105 dB range
            data_point = random.randint(81, 105)

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timeseries.append((current_time, data_point))  # Store the timestamp along with the data point
        print(f"Timestamp: {current_time} | Data point: {data_point} dB")
        time.sleep(1)  # Wait like a real sensor (should be 1 second etc. but speed up!!)

        # Convert 'timeseries' to a pd df_tS
        timestamps = [tS[0] for tS in timeseries]  # Extract the timestamps
        data = [tS[1] for tS in timeseries]  # Extract the data
        timestamps = pd.to_datetime(timestamps)  # Convert timestamps to pandas datetime format
        df_tS = pd.DataFrame({'Timestamp': timestamps, 'Data': data})

        # Could just Return: tS = timeseries... Do in another function to a database (InfluxDB, Prometheus, TimescaleDB)

        filename_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        df_tS.to_parquet(f"derivatives/tS_duration-{duration}_created-{filename_timestamp}.parquet")

    return df_tS
