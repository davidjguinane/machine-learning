import pandas as pd 
import numpy as np 

def imputation(filename):

    baseball = pd.read_csv(filename)
    baseball['weight'] = baseball['weight'].fillna(np.mean(baseball['weight']))
    print(baseball)
    return baseball

imputation('Master.csv')