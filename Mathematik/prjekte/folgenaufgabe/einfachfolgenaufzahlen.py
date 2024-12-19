def FolgeA(a1,  length):
    folgea = []
    previouselement = a1
    for n in range(1, length+1):
        if n == 1:
            an = a1
        else:
            an = (n-1) * previouselement + 1
        folgea.append(an)
        previouselement = an
    return (folgea)


def FolgeB(b1, length):
    folgeb = []
    previouselement = b1
    for n in range(1, length+1):
        if n == 1:
            bn = b1
        else:
            bn = (n-1) * previouselement - 1
        folgeb.append(bn)
        previouselement = bn
    return (folgeb)


lista1 = [3]
listb1 = [2]

# for a1 in lista1:
#    folgea = FolgeA(a1, 100)
#    descriptivefolgea = ()
#    for elementa in folgea:
#        if folgea.index(elementa) != 0:
#            ersteableitungan = elementa - folgea[folgea.index(elementa)+1]
#            ersteableitungena.append(ersteableitungan)
#        indexa = folgea.index(elementa)+1
#        descriptivea = (f'a{indexa} = {elementa}', )
#        descriptivefolgea += descriptivea


for a1 in lista1:
    ersteableitung = []
    folgea = FolgeA(a1, 10)
    descriptivefolgea = ()
    for elementa in folgea:
        if folgea.index(elementa) != 0:
            ersteableitungquotient = elementa - \
                folgea[folgea.index(elementa)-1]
           # print(ersteableitungquotient)
            ersteableitung.append(ersteableitungquotient)
        # print(folgea[folgea.index(elementa)-1])
        indexa = folgea.index(elementa)+1
        descriptivea = (f'a{indexa} = {elementa}', )
        descriptivefolgea += descriptivea
        # print(ersteableitung)

for quotient in ersteableitung:
    if ersteableitung.index(quotient) != 0:
        zweiteableitungquotient = quotient - \
            ersteableitung[ersteableitung.index(quotient)-1]
       # print(zweiteableitungquotient)

ersteableitungb = []
for b1 in listb1:
    print("")
    folgeb = FolgeB(b1, 10)
    descriptivefolgeb = ()
    for elementb in folgeb:
        if folgeb.index(elementb) != 0:
            ersteableitungquotient = elementb - \
                folgeb[folgeb.index(elementb)-1]
            # print(ersteableitungquotient)
            ersteableitungb.append(ersteableitungquotient)
        indexb = folgeb.index(elementb)+1
        descriptiveb = (f'b{indexb} = {elementb}', )
        descriptivefolgeb += descriptiveb

for quotient in ersteableitungb:
    if ersteableitungb.index(quotient) != 0:
        zweiteableitungquotient = quotient - \
            ersteableitungb[ersteableitungb.index(quotient)-1]
  #      print(zweiteableitungquotient)

print(descriptivefolgea)
print(descriptivefolgeb)
