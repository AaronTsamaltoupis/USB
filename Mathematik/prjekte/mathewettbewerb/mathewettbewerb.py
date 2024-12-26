import sys
import os
from math import factorial
path = r"C:\Users\User\Desktop\USBStick\Mathematik\prjekte data"
sys.set_int_max_str_digits(0)


folge = []


#for n in range(2, 1000):
#    decimal_n = str(factorial(n))
#    x = 1
#    while True:
#        potentialnewelement = decimal_n[len(decimal_n)-x]
#        potentialnewelement = int(potentialnewelement)
#        if potentialnewelement != 0:
#            folge.append(potentialnewelement)
#            break
#        else:
#            x += 1

#print(folge)
message ="" 
for n in range(2, 10000):
    message += str(factorial(n))
    message += "\n"
#    print(factorial(n))

print(message)
file  = open(os.path.join(path, "factorialnumbers.txt"), "w")
file.writelines(message)
file.close()
