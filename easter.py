#!/usr/bin/python

import sys
import math

#https://fr.wikipedia.org/wiki/Calcul_de_la_date_de_P%C3%A2ques_selon_la_m%C3%A9thode_de_Meeus
#Valid from year 1583
def butcherAlgoComputation(year):
    A = year
    #cycle de Meton
    N = A % 19
    #centaine et rang de l'annee                         
    U = A % 100
    #centaine et rang de l'annee                          
    C = int(math.floor(A / 100))
    #siecle bissextile
    S = int(math.floor(C / 4))
    #siecle bissextile
    T = C % 4
    #cycle de proemptose
    P = int(math.floor((C + 8) / 25))
    #proemptose
    Q = int(math.floor((C - P + 1) / 3))
    #epacte
    E = (19 * N + C - S - Q + 15) % 30
    #annee bissextile 
    B = int(math.floor(U / 4))
    #annee bissextile
    D = U % 4
    #lettre dominicale
    L = (2 * T + 2 * B - E - D + 32) % 7
    #correction
    H = int(math.floor((N + 11 * E + 22 * L) / 451 ))
    #mois et quantieme du Samedi saint
    M = int(math.floor((E + L - 7 * H + 114) / 31 ))
    #mois et quantieme du Samedi saint
    J = (E + L - 7 * H + 114) % 31
    return (J + 1, M)

# https://fr.wikipedia.org/wiki/Calcul_de_la_date_de_P%C3%A2ques_selon_la_m%C3%A9thode_de_Gauss
def gaussAlgoComputation(year):
    A = year % 19
    B = year % 4
    C = year % 7
    K = int(math.floor(year / 100))
    P = int(math.floor((13 + 8 * K) / 25))
    Q = int(math.floor(K / 4))
    M = (15 - P + K - Q) % 30
    N = (4 + K - Q) % 7
    D = (19 * A + M) % 30
    E = (2 * B + 4 * C + 6 * D + N) % 7
    MA = 22 + D + E
    MONTH = 4 if MA > 31 else 3
    DAY = MA if MA <= 31 else MA % 31
    if (D == 29 and E == 6):
        DAY = 19
        MONTH = 4
    if (D == 28 and E == 6 and ((11 * M + 11) / 30) < 19):
        DAY = 18
        MONTH = 4
    return (DAY, MONTH)

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
    if (year < 1583):
        raise ValueError("Year is valid beginning 1583")
    #gausAlgoComputation(year)
    butcherResult = butcherAlgoComputation(year)
    month = str(butcherResult[1]).zfill(2)
    day = str(butcherResult[0]).zfill(2)
    print "{}-{}-{}".format(year, month, day)
    
if (len(sys.argv) < 2):
    usage()
else:
    main(sys.argv[1])