__author__ = 'david_guinane'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# Read rocks versus mines data into pandas data frame
data = pd.read_csv(target_url,header=None, prefix="V")

for i in range(208):
	# Assign plot color based on "M" or "R" labels
	if data.iat[i,60] == "M":
		plot_color = "red"
	else:
		plot_color = "blue"
	# Plot rows of data as if there were Series data
	dataRow = data.iloc[i, 0:60]
	dataRow.plot(color=plot_color)

plot.xlabel("Attribute Index")
plot.ylabel(("Attribute Values"))
plot.show()
