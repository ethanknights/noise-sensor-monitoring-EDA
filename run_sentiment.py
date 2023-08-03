import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import statsmodels.api as sm


# Download the VADER lexicon (run this only once)
nltk.download('vader_lexicon')

def read_data():
    df = pd.read_excel('/Users/ethanknights/Desktop/Sprout Social Export (Westminster City Council) Oct 01, 2022 - Jan 26, 2023.xlsx')
    return df

df = read_data()

columns_to_keep = ['Timestamp (BT)', 'Message']
df.drop(columns=df.columns.difference(columns_to_keep), inplace=True)

df.dropna(inplace=True)

# Loop to calculate sentiment
# Create the VADER SentimentIntensityAnalyzer object
analyzer = SentimentIntensityAnalyzer()
sentiment_scores = []

for message in df['Message']:
    if pd.isna(message) or (isinstance(message, float) or isinstance(message, int)):
        score = {'compound': 0, 'neg': 0, 'neu': 0, 'pos': 0}
    else:
        score = analyzer.polarity_scores(message)
        sentiment_scores.append(score)


sentiment_df = pd.DataFrame(sentiment_scores)

np.min(sentiment_df['compound'])
np.max(sentiment_df['compound'])

# Add the sentiment scores DataFrame to the original DataFrame
df = pd.concat([df, sentiment_df], axis=1)




# Assuming you have your time series data in 'endogenous_data' and your exogenous variable data in 'exogenous_data'
# Both 'endogenous_data' and 'exogenous_data' should be pandas Series or DataFrames

# Create a SARIMAX model with your endogenous data and the exogenous variable
model = sm.tsa.SARIMAX(endogenous_data, order=(p, d, q), seasonal_order=(P, D, Q, S), exog=exogenous_data)

# Fit the model to the data
results = model.fit()

# Make predictions using the fitted model (you can use the exogenous variable for forecasting)
forecast_steps = 10  # Example: Forecast the next 10 time steps
forecast = results.get_forecast(steps=forecast_steps, exog=new_exogenous_data)
forecast_values = forecast.predicted_mean

