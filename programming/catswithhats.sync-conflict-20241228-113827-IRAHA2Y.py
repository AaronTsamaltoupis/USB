from random import *

numberhattedcats = 0

catvalues = {}

catnames = []

roundsandcats = 500

for catnumber in range(1,roundsandcats+1):
    catnames.append(str(catnumber))
    catvalues[str(catnumber)]=False


#print(catvalues)


#print(len(catnames))



for roundd in range(1,roundsandcats+1):
    #print(roundd)
    for catnumber in range(1,roundsandcats+1):
        if catnumber % roundd == 0:
            #print(catnumber)
            catvalues[list(catvalues)[catnumber-1]] = not catvalues[list(catvalues)[catnumber-1]]
    #        print("")

#print(catvalues)
catcounter = 0
catswithhats = []
catswithouthats = []

for cat in catvalues:
    if catvalues[cat] == True:
        catswithhats.append(cat)
    else:
        catswithouthats.append(cat)

print("cats with hats:")
print(catswithhats)
print("cats without hats: ")
print(catswithouthats)





