__author__ = 'david_guinane'
import numpy as np
import pylab
import scipy.stats as stats
import urllib2
import sys

# Using Anaconda

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urllib2.urlopen(target_url)

# Arrange List for Labels and Attributes
labels = []
xlist = []
for line in data:
	#Split on comma
	row = line.decode().strip().split(",")
	xlist.append(row)

# Generate summary statistics for column 3 (e.g.)
col = 3
colData = []

for row in xlist:
	colData.append(float(row[col]))

stats.probplot(colData, dist="norm", plot=pylab)
pylab.show()