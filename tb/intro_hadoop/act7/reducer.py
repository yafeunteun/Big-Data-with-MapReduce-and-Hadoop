#!/usr/bin/python

import sys

salesTotal = 0
counter = 0

for line in sys.stdin:
    thisSale = line.strip()

    salesTotal += float(thisSale)
    counter += 1

print counter,  "\t", salesTotal

