import os

import plotly.graph_objects as go
from tabulate import tabulate

path = "C:/Users/User/Dropbox/Mathematik/data"


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


head = ["b1/a1"]
bOnerow = []
allcommonelements = [bOnerow]


for a1 in range(1, 50):
    commonelementsan = []
    # commonelementsan enthaelt alle listen an gemeinsamen elementen, die das aktuelle an mit jedem bn hat
    # print(a1)
    for b1 in range(1, 50):
        if a1 == 1:
            #            bOnerow.append(f'b1 = {b1}')
            bOnerow.append(b1)
        if b1 == 1:
            #            head.append(f'a1={a1}')
            head.append(a1)
        commonelementsanbn = []
        # commonelementsanbn enthaelt die elemente, die das aktuelle a1 mit dem aktuellen b1 gemeinsam hat
        folgea = FolgeA(a1, 100)
        folgeb = FolgeB(b1, 100)
        for elementa in folgea:
            for elementb in folgeb:
                if elementb == elementa:
                    if elementa not in commonelementsanbn:
                        commonelementsanbn.append(elementb)
        # print(commonelements)
        commonelementsan.append(str(commonelementsanbn))
    allcommonelements.append(commonelementsan)


# for x in allcommonelements:
#    print(allcommonelements)
# message = tabulate(allcommonelements, headers=head, tablefmt="grid")
# print(head)
fig = go.Figure(data=[go.Table(header=dict(values=head),
                               cells=dict(values=allcommonelements))
                      ])
# print(message)


fig.show()

# print("")
# for x in allcommonelements:
#    print(allcommonelements)

# message = tabulate(allcommonelements, headers=head, tablefmt="grid")
# print(message)

# TableFile = open(os.path.join(path, "tablefileb1ontop.txt"), "w")

# TableFile.writelines(message)
# TableFile.close()
