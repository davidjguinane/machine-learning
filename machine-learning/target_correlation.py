__author__ = 'david_guinane'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from random import uniform

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# Read rocks versus mines data into pandas data frame
data = pd.read_csv(target_url,header=None, prefix="V")

# Change the targets to numeric values
target = []

for i in range(208):
	# Assign 0 or 1 target value based on "M" or "R" labels
	if data.iat[i,60] == "M":
		target.append(1.0)
	else:
		target.append(0.0)

# Plot 35th Attribute
dataRow = data.iloc[0:208,35]
plot.scatter(dataRow, target)

plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()

# To improve visualization, this version dithers the points
# a little and makes them somewhat transparent

target = []
for i in range(208):
	# Assign 0 or 1 target value based on "M" or "R" labels
	if data.iat[i, 60] == "M":
		target.append(1.0 + uniform(-0.1, 0.1))
	else:
		target.append(0.0 + uniform(-0.1, 0.1))

# Plot the 35th Attribute

dataRow = data.iloc[0:208, 35]
plot.scatter(dataRow, target, alpha=0.5, s=120)

plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()