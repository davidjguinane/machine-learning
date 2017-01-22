import pandas as pd 

# read the CSV file
baseball_data = pd.read_csv('Master.csv')

# print the column nameFirst
print(baseball_data['nameFirst'])

# Add a column by performing an operator on two existing columns
baseball_data['height_plus.weight']=baseball_data['height']+baseball_data['weight']

# write new column to CSV
baseball_data.to_csv('baseball_data_with_hieght_weight.csv')