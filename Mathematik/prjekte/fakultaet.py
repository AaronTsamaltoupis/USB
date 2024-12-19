import math
import sys
import os

sys.set_int_max_str_digits(0)


path ="/home/aaron/Desktop/USBStick/Mathematik/prjekte data"

message = ""
for n in range(1000):
    message += str(math.factorial(n))
    message += "\n"


file = open(os.path.join(path, "fakultaeten.txt"), "w")
file.writelines(message)

print(message)
