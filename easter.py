#!/usr/bin/python

import sys

def modulogo(year):
    A = year
    R = A % 4
    S = A % 7
    T = A % 19
    B = (19 * T) + 24
    M = B % 30
    C = (2 * R) + (4 * S) + (6 * M) + 5
    N = C % 7
    P = M + N
    if (P < 10):
        return (P + 22, 3)
    else:
        return (P - 9, 4)
    endif

def usage():
    print("Usage : ./easter.py [year]")
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
    value = modulogo(year)
    month = str(value[1]).zfill(2)
    day = str(value[0]).zfill(2)
    print "{}-{}-{}".format(year, month, day)
    
if (len(sys.argv) < 2):
    usage()
else:
    main(sys.argv[1])

## Source du projet : https://www.maths-et-tiques.fr/telech/PAQUES.pdf