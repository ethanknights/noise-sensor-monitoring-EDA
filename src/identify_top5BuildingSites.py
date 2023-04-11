# Purpose: Identify building site address info for top 5(?) sites (i.e. highest N registered complaints)

#
df = rawD  # Inherited dataframe sorted byDate (from setup/setup.py)


# Filter
df = df[df['Complaint Type'] == 'Building Site']
tmp = tmp.sort_values('Received Date')

# add regexp with 2022
tmp = tmp[tmp['Received Date'][7:] == '2022']
# len(tmp)
