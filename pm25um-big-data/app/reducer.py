#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

def main():
    current_job_location = None
    current_count = 0

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        job_location, count = line.split("\t", 1)

        try:
            count = int(count)
        except:
            continue

        if current_job_location == job_location:
            current_count += count
        else:
            if current_job_location is not None:
                print("%s\t%d" % (current_job_location, current_count))
            current_job_location = job_location
            current_count = count

    # output final group
    if current_job_location is not None:
        print("%s\t%d" % (current_job_location, current_count))

if __name__ == "__main__":
    main()
