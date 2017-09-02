__author__ = 'david_guinane'
import urllib.request
import sys

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

for col in range(ncol):
	for row in xlist:
		try:
			a = float(row[col])
			if isinstance(a, float):
				type[0] += 1
		except ValueError:
			if len(row[col]) > 0:
				type[1] += 1
			else:
				type[2] += 1
		
	colcounts.append(type)
	type = [0]*3

sys.stdout.write("Col#" + '\t' + "Number" + '\t' + "Strings" + '\t ' + "Other\n")

iCol = 0
for types in colcounts:
	sys.stdout.write(str(iCol) + '\t\t' + str(types[0]) + '\t\t' + str(types[1]) + '\t\t' + str(types[2]) + "\n")
	iCol += 1