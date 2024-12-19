from math import factorial

import matplotlib.pyplot as plt
import numpy as np
from mpl_interactions import ioff, panhandler, zoom_factory

import graph


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


def FolgehatElement(element, position):
    summe = 0
    for i in range(2, position):
        summe += factorial(position-1)/(i*(position-1))
    b1 = element+1+summe
    return (b1)


def KuenstlicheFolge(bk, k, length):
    kuenstlichefolge = []
    previouselement = bk
    for n in range(k, length+1):
        if n == k:
            bn = bk
        else:
            bn = (n-1) * previouselement - 1
        kuenstlichefolge.append(bn)
        previouselement = bn
    return (kuenstlichefolge)


length = 6
selectiona1 = [4, 0]
selectionb1 = [4]
selectionkuenstlichb1 = []


fig = plt.figure()
ax = fig.add_subplot(111, xlim=(0, 1), ylim=(0, 1), autoscale_on=False)

xaxis = np.array(range(1, length+1))
for a1 in selectiona1:
    yaxis = np.array(FolgeA(a1, length))
    # print(f'a1 = {a1}')
    # print(f'folge a={FolgeA(a1, length)}')
    ax.plot(xaxis, yaxis, "o")


for y in FolgeA(4, length):
    for x in range(1, length):
        selectionkuenstlichb1.append((y, x))

print(selectionkuenstlichb1)
for b1 in selectionb1:
    yaxis = np.array(FolgeB(b1, length))
    # print(f'b1 ={b1}')
    # print(f'folge b = {FolgeB(b1, length)}')
    plt.plot(xaxis, yaxis, "or")
    plt.xlabel('a1bn')
    plt.ylabel('wert von folge')


# kuenstlichefolge
for bk in selectionkuenstlichb1:
    yaxxis = []
#    print(bk[1])
    for x in range(1, bk[1]):
        yaxxis.append(0)
    for y in KuenstlicheFolge(bk[0], bk[1], length):
        yaxxis.append(y)
#    print(f'b{bk[1]} = {bk[0]}')
#    print(yaxxis)
    plt.plot(xaxis, yaxxis, ".")

scale = 1.1
zp = graph.ZoomPan()
figZoom = zp.zoom_factory(ax, base_scale=scale)
figPan = zp.pan_factory(ax)
amatrix = []
for a1 in selectiona1:
    print(f'a1 = {a1}: ', FolgeA(a1, length))
    amatrix.append(FolgeA(a1, length))
bmatrix = []
for b1 in selectionb1:
    print(f'b1 = {b1}: ', FolgeB(b1, length))
    bmatrix.append(FolgeB(b1, length))
kmatrix = []
yaxxis = []
for bk in selectionkuenstlichb1:
    for x in range(1, bk[1]):
        yaxxis.append(0)
    for y in KuenstlicheFolge(bk[0], bk[1], length):
        yaxxis.append(y)
    print(f'b{bk[1]} = {bk[0]}: ', yaxxis)
    kmatrix.append(yaxxis)
    yaxxis = []

for listc in kmatrix:
    for bk in listc:
        if bk < amatrix[0][listc.index(bk)] and bk > amatrix[1][listc.index(bk)]:
            print("error")
            print(listc, bk)
            print("")
            print(amatrix[0])
            print(bmatrix[0])
            print(amatrix[1])
            print("")
            print(amatrix[0])
            print(listc)
            print(amatrix[1])
            print("")
            print("")


plt.show()


# for an in list(xaxis):
#    valuean = []
#    for a1 in selectiona1:
#        valuean.append(FolgeA(a1, length)[an-1])
#    print('lolol')
#    print(valuean)
