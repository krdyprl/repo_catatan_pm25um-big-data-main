#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import csv

def read_input(file):
    # csv.reader handles quotes, embedded commas, etc.
    reader = csv.reader(file)
    for row in reader:
        yield row

def main():
    first_line = True
    for row in read_input(sys.stdin):
        # Skip header
        if first_line:
            first_line = False
            continue

        # Ensure row has enough columns
        # job_location column exists in dataset
        try:
            job_location = row[7]  # change index if needed
        except:
            continue

        if job_location is None:
            continue

        job_location = job_location.strip()
        if job_location == "":
            continue

        print("%s\t1" % job_location)

if __name__ == "__main__":
    main()

