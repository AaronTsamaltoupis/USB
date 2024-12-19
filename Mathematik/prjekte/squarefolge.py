import math
import os
path = "/media/Aaron/USBStick/Mathematik/prjekte data"
Data = open(os.path.join(path, "squarefolgedata.txt"), "w")
Data.close()
Data = open(os.path.join(path, "squarefolgedata.txt"), "a")
for x in range(100):
    f = x + math.sqrt(x) + 1/2
    message = f'\n{f} {math.floor(f)}'
    Data.writelines(message)
    print(message)

Data.close()
    
