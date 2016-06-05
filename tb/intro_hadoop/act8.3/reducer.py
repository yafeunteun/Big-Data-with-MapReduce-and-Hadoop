#!/usr/bin/python

import sys

oldKey = None
counter = 0
max_count = 0
max_key = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data = line.strip()

    thisKey = data

    if oldKey and oldKey != thisKey:
	if counter > max_count:
            max_count = counter
            max_key = oldKey        
        oldKey = thisKey;
        counter = 0

    oldKey = thisKey
    counter += 1

if oldKey != None:
    print max_key, "\t", max_count

