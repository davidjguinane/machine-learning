__author__ = 'david_guinane'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# Read rocks versus mines data into pandas data frame
data = pd.read_csv(target_url,header=None, prefix="V")

# Print head and tail of data frame
print(data.head())
print(data.tail())

#Print summary of data frame
summary = data.describe()
print(summary)