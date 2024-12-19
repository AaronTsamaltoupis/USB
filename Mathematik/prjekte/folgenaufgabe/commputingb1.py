
x = ""

folgeb = [3, x, 5, x]


for element in folgeb:
    if type(element) == int:
        positionelement = folgeb.index(element)+1
        print(positionelement)
