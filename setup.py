import pandas as pd
import sys
from datetime import datetime


def read_data():
    """
    Return dataframe of all complaints.

    :return: rawD: (Currently via loading hardcoded data path locally)
    :rtype: pd.dataframe
    """

    rawD = pd.read_csv('./data/raw_April2023_1997-2023.csv')

    return rawD


def convert_raw_date_time(df):
    """
    Return dataframe where datetime string columns are converted to datetime objects according to:
    - 'Received Date' (yyyy-mm-dd)
    - 'Received Time' (HH:MM or pd.NaT)

    :param df: Dataframe including 'Received Date' and 'Received Time' columns.
    :return: df: Return dataframe
    :rtype: pd.dataframe
    """

    if df['Received Date'].iloc[0][2] == '/':  # If df still in raw format (dd/mm/yyyy)

        df['Received Date'] = df['Received Date'].apply(
            lambda x: datetime.strptime(x, '%d/%m/%Y').date())

        df['Received Time'] = df['Received Time'].apply(
            lambda x: pd.NaT if x == 'XXXX' else datetime.strptime(x, '%H:%M').time())

    return df


# EXTRA FUNCTIONS
def extra_print_unique_data(df):
    """
    EXTRA TEMPORARY!    Print unique values from a dict

    :param df: Dataframe including 'Received Date' and 'Received Time' columns.
    :return: unique_values_dict: Dictionary with key per column, and all of the column's unique values
    :rtype: dict
    """

    # Print unique values to get dataset gist
    unique_values_dict = {}
    for col in df.columns:
        unique_values_dict[col] = df[col].unique()
    print("\n\n\nUnique values in column {}: {}\n".format(col, unique_values_dict))
    sys.getsizeof(unique_values_dict)
    print(unique_values_dict['Complaint Type Code'])
    print(unique_values_dict['Complaint Type'])
    print(unique_values_dict['Complaint Sub Type'])
    print(unique_values_dict['AddressKey'][0:9])

    return unique_values_dict
