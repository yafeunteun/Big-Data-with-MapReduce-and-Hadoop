#!/usr/bin/python

import sys

counter = 0
oldKey = None


for line in sys.stdin:
    ip = line.strip()

    thisKey = ip

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", counter 
        oldKey = thisKey;
        counter = 0

    oldKey = thisKey
    counter += 1 

if oldKey != None:
    print oldKey, "\t", counter 

