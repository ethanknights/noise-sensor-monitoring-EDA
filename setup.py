import pandas as pd
import sys
from datetime import datetime


def describe_data(df):
    """
    Print nRows (i.e. complaints in dataframe).

    :param df: df: From read_data()
    """
    print(f"Current nRows in memory: {df.shape[0]}\n")
    return


def read_data():
    """
    Return dataframe of all complaints.

    :return: rawD: (Currently via loading hardcoded data path locally)
    :rtype: pd.dataframe
    """

    df = pd.read_csv('./data/raw_April2023_1997-2023.csv')
    print('Loaded data as: df')
    describe_data(df)

    return df


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


def remove_missing_date_rows(df):
    """
    Return dataframe with NaT values dropped

    :param df: Dataframe including 'Received Time' columns.
    :return: df: Return dataframe
    :rtype: pd.dataframe
    """
    na_rows = df[df['Received Time'].isna()]

    print(f"Dropping {na_rows.shape[0]} rows with NaT in 'Received Time' column:")
    print(na_rows)

    df.drop(na_rows.index, inplace=True)

    describe_data(df)

    return df


def create_joined_datetime(df):
    """
    Return dataframe with 'datetime' column appended after 'Date Received' which
    concatenates 'Received Date' (yyyy-mm-dd) & 'Received Time' (HH:MM or pd.NaT)

    :param df: Dataframe including 'Received Date' and 'Received Time' columns.
    :return: df: Return dataframe
    :rtype: pd.dataframe
    """
    df['Received DateTime'] = pd.to_datetime(df['Received Date'].astype(str) + ' ' + df['Received Time'].astype(str))

    def change_column_order(df, col_name, index):
        cols = df.columns.tolist()
        cols.remove(col_name)
        cols.insert(index, col_name)
        return df[cols]
    col_names = df.columns.tolist()
    idx = col_names.index('Received Time')
    df = change_column_order(df, 'Received DateTime', idx + 1)

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
