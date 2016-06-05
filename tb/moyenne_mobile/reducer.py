#!/usr/bin/python
# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab
import sys

# Window size for moving average
win = 25
cpt = 0
oldKey = None
marketTotal = 0.0
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		# Something has gone wrong. Skip this line.
		continue

	thisKey, thisStock = data_mapped

	if oldKey and oldKey != thisKey:
		cpt += 1
		if(cpt > win):
			cpt = 0
			print marketTotal / win
			marketTotal = 0
		oldKey = thisKey;
			

	oldKey = thisKey
	cpt += 1
	try:
		marketTotal += float(thisStock)
	except:
		None

if oldKey != None:
	print marketTotal / win
