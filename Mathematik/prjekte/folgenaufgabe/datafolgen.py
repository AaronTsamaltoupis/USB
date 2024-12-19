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


allcommonelements = []

rangea1 = 100

for a1 in range(1, rangea1):
    commonelementsfora1 = []
#    print(a1)
    for b1 in range(1, 100):
        dataInputFile = open("datafolgen.txt", "a")
        commonelements = []
        folgea = FolgeA(a1, 10)
        folgeb = FolgeB(b1, 10)
        for elementa in folgea:
            for elementb in folgeb:
                if elementb == elementa:
                    # commonelements.append((elementa, folgea.index(elementa), folgeb.index(elementb)))
                    if elementa not in commonelements:
                        commonelements.append(elementa)
#        print(commonelements)
        dataInputFile.writelines(str(commonelements))
        commonelementsfora1.append(commonelements)

    dataInputFile.close()
    dataInputFile = open("datafolgen.txt", "a")
    dataInputFile.writelines("\n")
    dataInputFile.close()
    allcommonelements.append(commonelementsfora1)
#    print("")
