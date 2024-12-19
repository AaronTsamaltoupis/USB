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


for a1 in range(0, 35):
    # print(a1)
    for b1 in range(0, 35):
        commonelements = []
        folgea = FolgeA(a1, 100)
        folgeb = FolgeB(b1, 100)
        for elementa in folgea:
            for elementb in folgeb:
                if elementb == elementa:
                    indexa = folgea.index(elementa)
                    indexb = folgeb.index(elementb)
#                    if elementa not in commonelements:
#                        commonelements.append(elementa)
                    commonelements.append(elementa)
                    print(a1, b1, commonelements,
                          (f'a{indexa+1}', f'b{indexb+1}'))
