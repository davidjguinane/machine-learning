__author__ = 'david_guinane'
import urllib.request
import sys
import numpy as np

# Read data from the UCI Data Repository
data = urllib.request.urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# Arrange List for Labels and Attributes
labels = []
xlist = []
for line in data:
	#Split on comma
	row = line.decode().strip().split(",")
	xlist.append(row)

sys.stdout.write("Number of Rows of Data = " + str(len(xlist)) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(len(xlist[1])) + '\n')

nrow = len(xlist)
ncol = len(xlist[1])

type = [0]*3
colcounts = []

'''
Generate summary stats for Column 3
'''
col = 3
colData = []
for row in xlist:
	colData.append(float(row[col]))

colArray = np.array(colData)
colMean = np.mean(colArray)
colStd = np.std(colArray)

sys.stdout.write("Mean = " + '\t' + str(colMean) + '\t\t' + "Standard Deviation = " + '\t' + str(colStd) + "\n")

# Calculate Quantile Boundaries
ntiles = 4
percentbdry = []

for i in range(ntiles+1):
	percentbdry.append(np.percentile(colArray, i*(100)/ntiles))

sys.stdout.write("\nBoundaries for 4 Equal Percentiles \n")
print(percentbdry)
sys.stdout.write(" \n")

# Run again with 10 equal intervals
ntiles = 10
percentbdry = []

for i in range(ntiles+1):
	percentbdry.append(np.percentile(colArray, i*(100)/ntiles))

sys.stdout.write("Boundaries for 10 Equal Percentiles \n")
print(percentbdry)
sys.stdout.write(" \n")

# The last column contains categorical variables
col = 60
colData = []

for row in xlist:
	colData.append(row[col])
	unique = set(colData)

sys.stdout.write("Unique Label Values \n")
print(unique)

# Count up the number of elements having each value
catDict = dict(zip(list(unique),range(len(unique))))
catCount = [0]*2

for elt in colData:
	catCount[catDict[elt]] += 1

sys.stdout.write("\nCounts for Each Value of Categorical Label \n")
print(list(unique))
print(catCount)