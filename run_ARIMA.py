import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def read_data():
    df = pd.read_csv('DWH-Noise_2022-2023.csv')
    return df

def convert_df_to_timeseries(df):
    df = df.groupby('Received Date').size().reset_index(name='Frequency')
    return df

def preprocess_df(df):

    print(f'WARNING: Converting date column to datetime')
    df['Received Date'] = pd.to_datetime(df['Received Date'])
    df['Received Date'] = df['Received Date'].dt.date

    print(f'WARNING: Dropping hardcoded date:')
    date_to_drop = pd.to_datetime('2023-07-19')
    print(date_to_drop)
    df.drop(df[df['Received Date'] == date_to_drop].index, inplace=True)

    return df


def apply_MAD_filter(df):

    print(f'WARNING: Applying MAD Filter')

    num_rows_before = len(df)

    # Method 1
    # mad_threshold = 3.2
    # median = df['Frequency'].median()
    # mad = (df['Frequency'] - df['Frequency'].mean()).abs().mean()
    # df_filtered = df[
    #     (df['Frequency'] >= median - mad_threshold * mad) & (df['Frequency'] <= median + mad_threshold * mad)]

    # Method 2
    mad_threshold_percentile = 0.5  # Aggressive to get rid of the 1 case with huge >100 spike
    median = df['Frequency'].median()
    mad = (df['Frequency'] - df['Frequency'].mean()).abs().mean()
    mad_threshold = mad * pd.Series.quantile(pd.Series.abs(df['Frequency'] - median), mad_threshold_percentile)
    df_filtered = df[
        (df['Frequency'] >= median - mad_threshold) & (df['Frequency'] <= median + mad_threshold)]

    # Log the number of rows after filtering
    num_rows_after = len(df_filtered)

    # Log the number of rows affected
    num_rows_affected = num_rows_before - num_rows_after
    print(f'Number of rows affected by MAD filter: {num_rows_affected}')

    return df_filtered


def do_lineplot(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Received Date'], df['Frequency'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Frequency')
    plt.title('Complaints Per Day')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return


def perform_adf_test(timeseries):
    result = adfuller(timeseries)
    print("Stationarity Test for Original Data:")
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print(f'   {key}: {value}')
    return result


def do_ACF_PACF_plots(timeseries):
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plot_acf(df['Frequency'], lags=30, ax=plt.gca())
    plt.subplot(2, 1, 2)
    plot_pacf(df['Frequency'], lags=30, ax=plt.gca())
    plt.tight_layout()
    plt.show()
    return


# Gathering dataset
df = read_data()
df = convert_df_to_timeseries(df)
df = preprocess_df(df)
do_lineplot(df)

df = apply_MAD_filter(df)
do_lineplot(df)


# Test if differencing is required (is stationarity assumption met?)
adf_result = perform_adf_test(df['Frequency'])
# No differencing required:
# Stationarity Test for Original Data:
# ADF Statistic: -3.2594732712132406
# p-value: 0.016790107977829122
# Critical Values:
#    1%: -3.442295604706236
#    5%: -2.866809328264463
#    10%: -2.569576376859504
do_ACF_PACF_plots(df)

# ARIMA modeling
df.set_index('Received Date', inplace=True) # required datetime index
df.index.freq = 'D'  # Set the frequency to 'D' for daily data

# Replace p, d, and q with the identified values of autoregressive lags, differencing, and moving average lags
p = 1
d = 0
q = 1

# Replace seasonal_p, seasonal_d, and seasonal_q with the identified values of seasonal autoregressive lags, seasonal differencing, and seasonal moving average lags (which are all zeros in this case)
seasonal_p = 1
seasonal_d = 0
seasonal_q = 0

# Set the seasonal period to 6 (since you identified the seasonal pattern with a period of 6)
seasonal_period = 6

# Create the ARIMA model with seasonal components
model = ARIMA(df['Frequency'], order=(p, d, q), seasonal_order=(seasonal_p, seasonal_d, seasonal_q, seasonal_period))


result = model.fit()

# Forecasting
forecast_horizon = 10  # Replace this with the number of periods you want to forecast
forecast = result.forecast(steps=forecast_horizon)

# Plot the forecast
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Frequency'], marker='o', label='Actual')
plt.plot(pd.date_range(start=df.index[-1], periods=forecast_horizon+1, closed='right'), forecast, marker='o', linestyle='dashed', label='Forecast')
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.title('ARIMA Forecast')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()












