import pandas as pd
import hashlib

df = pd.read_excel('/Users/ethanknights/Desktop/Noise Repeat Complaints-Ethan_Jul-Case-Matching.xlsx')

#df = df[df["CustomerName"] != "Not Recorded"]

# Count duplicates in the "CustomerReference" column
duplicate_counts = df["anonymized_name"].value_counts()
# No duplicates found in Customer Reference

def anonymize_field(name):
    name = str(name)

    if name.lower() != "not recorded":
        # Hash the customer name using MD5 (or any other hash algorithm)
        hash_object = hashlib.md5(name.encode())
        hashed_name = hash_object.hexdigest()
        return hashed_name[:10]  # Return the first 10 characters of the hash
    else:
        return name  # Return the original name if it matches "Not Recorded"

df["anonymized_name"] = df["CustomerName"].apply(anonymize_field)

df["anonymized_UPRN"] = df["UPRN"].apply(anonymize_field)

df = df.drop("CustomerName", axis=1)
df = df.drop("UPRN", axis=1)
df = df.drop("Unnamed: 9", axis=1)

df.to_csv("DWH-Noise_2022-2023.csv", index=False)


# row_indices = duplicate_counts.iloc[:].index
tmp = df[df["anonymized_name"] == row_indices[0]]