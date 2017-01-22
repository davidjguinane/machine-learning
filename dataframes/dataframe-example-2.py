import numpy as np
import pandas as pd

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions','Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}

football = pd.DataFrame(data)

print(football)
print(football.dtypes) # returns the datatype for each column
print(football.describe) # 
print(football.head()) # prints first five rows of dataset
print(football.tail()) # prints last five rows of dataset
print(football['year'])
print(football.year)  # shorthand for football['year'] 
print(football.iloc[[0]]) #returns row zero
print(football.loc[[0]]) #returns row zero
print(football[3:5]) # returns an index between 3 and 5, excluding 5 (returns 3 and 4)
print(football[football.wins > 10]) #returns records where the wins are greater than 10
print(football[(football.wins > 10) & (football.team == "Packers")]) #only returns packers records where the wins are greater than 10