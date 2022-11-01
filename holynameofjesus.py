#!/usr/bin/python

import sys
import datetime

def usage():
    print("Usage : ./holynameofjesus.py [year]")
    print("Return an ISO 8601 date")

def main(stryear):
    year = 0
    try:
        year = int(stryear)
    except:
        usage()
        return
    if (year < 1900 or year > 2099):
        raise ValueError("Year is valid from 1900 to 2099")
    SDATE = datetime.datetime(year, 1, 5) ##Must be before the 6th of January
    WEEKDAY = int(SDATE.strftime("%w"))
    DAY = 5 - WEEKDAY
    if DAY < 2: ##Must be after the 1st of January
        DAY = 2
    EDATE = datetime.datetime(year, 1, DAY)
    print "{}-01-{}".format(year, EDATE.strftime("%d"))
    
if (len(sys.argv) < 2):
    usage()
else:
    main(sys.argv[1])