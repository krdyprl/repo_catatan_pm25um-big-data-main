#!/usr/bin/env python2
import sys
import csv

reader = csv.reader(sys.stdin)
header = True

for row in reader:
    if header:
        header = False
        continue

    company = row[6].strip()
    job_type = row[13].strip()

    if company and job_type:
        # composite key: company|job_type
        key = "%s|%s" % (company, job_type)
        print("%s\t1" % key)
