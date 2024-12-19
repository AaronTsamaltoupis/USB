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


dataInputFile = open("datafolgen.txt", "w")


allcommonelements = []

rangea1 = 100

for a1 in range(1, rangea1):
    commonelementsfora1 = []
#    print(a1)
    for b1 in range(1, 1000):
        commonelements = []
        folgea = FolgeA(a1, 100)
        folgeb = FolgeB(b1, 100)
        for elementa in folgea:
            for elementb in folgeb:
                if elementb == elementa:
                    # commonelements.append((elementa, folgea.index(elementa), folgeb.index(elementb)))
                    if elementa not in commonelements:
                        commonelements.append(elementa)
#        print(commonelements)
        commonelementsfora1.append(commonelements)
    allcommonelements.append(commonelementsfora1)
#    print("")

message = ""
for a1 in range(1, rangea1):
    message += (f'a1 = {a1},')

message = message[0:len(message) - 1]

dataInputFile.writelines(message)
dataInputFile.close()

dataInputFile = open("datafolgen.txt", "a")

for n in range(1, len(allcommonelements)+1):
    dataInputFile.writelines("\n")
    print(n, "th element")
    for commonelementsan in allcommonelements:
        print(commonelementsan[n-1])
        dataInputFile.writelines(f'{commonelementsan[n-1]},')

dataInputFile.close()
