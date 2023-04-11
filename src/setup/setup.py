import pandas as pd

def readData():
    # Read
    rawD = pd.read_csv('./data/raw_April2023_1997-2023.csv')
    rawD = rawD.sort_values('Received Date')

    # Print unique values to get dataset gist
    unique_values_dict = {}
    for col in rawD.columns:
        unique_values_dict[col] = rawD[col].unique()
    # print("\n\n\nUnique values in column {}: {}\n".format(col, unique_values_dict))
    # sys.getsizeof(unique_values_dict)
    print(unique_values_dict['Complaint Type Code'])
    print(unique_values_dict['Complaint Type'])
    print(unique_values_dict['Complaint Sub Type'])
    print(unique_values_dict['AddressKey'][0:9])

    # Analysis scripts next:
    print('Next:\npython ../identify_top5BuildingSites.py')

    return rawD
