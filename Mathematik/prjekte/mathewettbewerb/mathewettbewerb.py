import sys
import os
from math import factorial
path = "/home/aaron/Desktop/USB/Mathematik/prjekte data/"
sys.set_int_max_str_digits(0)





message ="" 
for n in range(1, 100):
    factorialstoprint = 5*n-1
    factorialstoprint2 = 5*n
    message += f'{factorialstoprint}! '
    message += str(factorial(factorialstoprint))
    message += "\n"
    message += f'{factorialstoprint2}! '
    message += str(factorial(factorialstoprint2))
    message += "\n"
#    print(factorial(n))

folge = []
for n in range(2, 1000):
    decimal_n = str(factorial(n))
    x = 1
    while True:
        potentialnewelement = decimal_n[len(decimal_n)-x]
        potentialnewelement = int(potentialnewelement)
        if potentialnewelement != 0:
            folge.append(potentialnewelement)
            break
        else:
            x += 1
print(folge)


for element in folge:
        if folge[folge.index(element)+1] == element:
            if folge[folge.index(element)+2]== element:
                print(folge.index(element))

#print(folge)

file  = open(os.path.join(path, "factorialfolge.txt"), "w")
file.writelines(message)
file.close()
