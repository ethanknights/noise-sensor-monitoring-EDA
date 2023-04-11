df_buildingComplaints = df[df['Complaint Type'] == 'Building Site']
tmp = tmp.sort_values('Received Date')

# add regexp with 2022
tmp = tmp[tmp['Received Date'][7:] == '2022']
# len(tmp)
