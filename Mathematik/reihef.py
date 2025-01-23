import math


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


for m in range(1,10):
    y = 0
    startpoint = m
    produkt = startpoint
    while True:
        if letzteZiffer(produkt) != 6:
            y+= 1
            produkt*= (startpoint+y)
        else:
            print(f'm={m},{startpoint}-{startpoint+y}')
            break



