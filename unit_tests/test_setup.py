import pandas as pd
import datetime
import unittest
import setup


class TestDataFrame(unittest.TestCase):

    def test_dtype_convert_received_datetime(self):
        """
        Test that 'Received Date' & 'Received Time' columns in the input DataFrame are
        correctly converted to datetime.date/time/datetime objects.

        - First, it reads input data using the 'setup.read_data' function and asserts all column values are strings.
        - Next, it applies the 'setup.convert_raw_date_time' function to convert the string columns to datetime objects.
        - Finally, it asserts that:
            (1) All date values in the 'Received Date' column are datetime.date objects.
            (2) All non-null time values in the 'Received Time' column are datetime.time objects.
                Non-null are used due to some missing data represented as 'NaT'
        - An additional assertion is included for the 'Received DateTime' column.

        If the test fails, an AssertionError is raised.
        """
        df = setup.read_data()
        self.assertTrue(df['Received Date'].apply(lambda x: isinstance(x, str)).all(),
                        "df['Received Date'] is not of type datetime.time")
        self.assertTrue(df['Received Time'].apply(lambda x: isinstance(x, str)).all(),
                        "df['Received Time'] is not of type datetime.time")

        df = setup.convert_raw_date_time(df)
        self.assertTrue(df['Received Date'].apply(lambda x: isinstance(x, datetime.date)).all(),
                        "df['Received Date'] contains values that are not of type datetime.time")
        self.assertTrue(df['Received Time'].apply(lambda x: isinstance(x, datetime.time) if pd.notna(x) else True).all(),
                        "df['Received Time'] contains values that are not of type datetime.time")

        df = setup.remove_missing_date_rows(df)
        df = setup.create_joined_datetime(df)
        self.assertTrue(df['Received DateTime'].apply(lambda x: isinstance(x, datetime.datetime)).all(),
                        "df['Received Date'] contains values that are not of type datetime.datetime")

if __name__ == '__main__':
    unittest.main()
