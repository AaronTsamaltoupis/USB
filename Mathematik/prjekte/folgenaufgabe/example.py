import numpy as np

lissst = []


# for x in list(np.arange(-5.0, float(10), 0.5).flatten):
#    lissst.append(x)
#
#
# print(lissst)


lissst = np.arange(1, 2, 0.5).tolist()
print(lissst)


for x in lissst:
    print(x)
