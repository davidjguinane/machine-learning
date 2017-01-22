import pandas as pd 

def add_full_name(path_to_csv, path_to_new_csv):

	read_data = pd.read_csv(path_to_csv)
	read_data['nameFull'] = read_data['nameFirst'] + read_data['nameLast']
	read_data.to_csv(path_to_new_csv)

add_full_name('Master.csv', 'Master_edited.csv')