import os
import math

path = "/home/aaron/Desktop/USB/Mathematik/prjekte data"

m = 4
#print(factorial(m*5))
#print("")

message1 = ""
for number in range(1,m*5+1):
    message1 += str(number)
    if number != m*5:
        message1 += "*"
    else: 
        message1 += f'={math.factorial(m*5)}'


with open(os.path.join(path, "regularfactorial.txt"), "w") as myFile:
    myFile.writelines(message1)


message2 = "hallo"

exponentlist = [m]
exponentlist = []
exponent = m


actualexponentsum = m
##calculate extraction of 5
#while True: 
#    potentialnewexponent = math.floor(exponent/5)
#
#    if potentialnewexponent!= 0:
#        exponentlist.append(potentialnewexponent)
#        exponent =potentialnewexponent
#        actualexponentsum += exponent
#    else:
#        rest = math.factorial(exponent)
#        break

while True: 
    potentialnewexponent = math.floor(exponent/5)

    if potentialnewexponent!= 0:
        exponentlist.append(potentialnewexponent)
        exponent =potentialnewexponent
        actualexponentsum += exponent
    else:
        entirety = 5*m
        for factor in range(1,math.floor((5*m-1)/5)+1):
            entirety*= 5*factor 

        rest = entirety/ 5**(actualexponentsum)
        break


ergebnis = 5**(actualexponentsum)*int(rest)

#print(ergebnis)

##calculate factorial(5m-1) without the fives
factorialwithoutfives = []
withoutfives = 1
for x in range(1, 5*m):
    if x%5 != 0:
#        print(x)
        factorialwithoutfives.append(x)
        ##add to ergebnis
        ergebnis*= x
        withoutfives *= x
#        print(ergebnis)

print(int(ergebnis))
print(math.factorial(5*m))
#print(5**6 * math.factorial(4)*withoutfives)





#extracting the twos:













#message2 ='5**(m)'
#
#for x in exponentlist:
#    message2+= f'+{x}'
#
#for x in range(1, exponent+1):
#    message2+= f'*{x}'
#
#
#for number in factorialwithoutfives:
#    message2 += f'* {number}'
#
#print(math.factorial(m*5))
#print(message2)
#
#with open(os.path.join(path, "regularfactorial.txt"), "a") as myFile:
#    myFile.writelines(f'\n{message2}')
