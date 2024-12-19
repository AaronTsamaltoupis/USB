import os

# import module
from tabulate import tabulate

path = r"C:\Users\User\Dropbox\Mathematik\data"


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


lowesta1 = (-20)
lowestb1 = lowesta1*2
head = ['b1/a1']
allcommonelements = []


for b1 in range(lowestb1, -lowestb1):
    commonelementsbn = []
    # commonelementsan enthaelt alle listen an gemeinsamen elementen, die das aktuelle an mit jedem bn hat
    # print(a1)
    for a1 in range(lowesta1, -lowesta1):
        if b1 == lowestb1:
            head.append("")
        commonelementsanbn = []
        # commonelementsanbn enthaelt die elemente, die das aktuelle a1 mit dem aktuellen b1 gemeinsam hat
        folgea = FolgeA(a1, 10)
        folgeb = FolgeB(b1, 10)
        for elementb in folgeb:
            for elementa in folgea:
                if elementb == elementa:
                    if elementa not in commonelementsanbn:
                        commonelementsanbn.append(elementa)
        if commonelementsanbn != []:
            commonelementsbn.append("x")
        else:
            commonelementsbn.append("")
        # print(commonelements)
        if a1 == lowesta1:
            commonelementsbn.append("")
#        commonelementsbn.append(str(commonelementsanbn))
    allcommonelements.append(commonelementsbn)


# for x in allcommonelements:
#    print(allcommonelements)


# print(message)

# print("")
print(head)
# for x in allcommonelements:
#    print(allcommonelements)

# print(head)
message = tabulate(allcommonelements, headers=head)
# print(message)

#######################################################################
TableFile = open(os.path.join(path, "tablefileb1ontopxx.txt"), "w")

TableFile.writelines(message)
TableFile.close()
