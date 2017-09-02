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