import math
import sys
import os

sys.set_int_max_str_digits(0)
def letzteZiffer(n):
    decimal_n = str(n)
    x = 1
    while True:
        potentialnewelement = decimal_n[len(decimal_n)-x]
        potentialnewelement = int(potentialnewelement)
        if potentialnewelement != 0:
            letzteziffer = potentialnewelement
            break
        else:
            x += 1

    return letzteziffer




message = ""
folge = ""
for n in range(1,200):
    #message += str(math.factorial(6*n))
    #message += "\n"
    folge  += str(letzteZiffer(math.factorial(n)))
    folge += ""
#print(message)
print(folge)

