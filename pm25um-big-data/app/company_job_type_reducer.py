#!/usr/bin/env python2
import sys

current_key = None
count = 0

for line in sys.stdin:
    key, value = line.strip().split("\t")
    value = int(value)

    if current_key == key:
        count += value
    else:
        if current_key:
            print("%s\t%d" % (current_key, count))
        current_key = key
        count = value

# last key
if current_key:
    print("%s\t%d" % (current_key, count))
