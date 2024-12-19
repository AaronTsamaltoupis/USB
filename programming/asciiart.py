import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import numpy as np
import os




root  = tk.Tk()
root.title("ascii art to nvim")
root.geometry("800x600")
#root.iconbitmap(r"G:\Meine Ablage\USBStick\programmng\luigimangione.ico")

rawascii = tk.StringVar()
dimensions = tk.StringVar()
filename = tk.StringVar()
processedascii = tk.StringVar()



widthrawascii = 0
heightrawascii = 0


##--------------------------------------------------
def buttonclicked():
    processedascii.set("")

    strinng = dimensions.get()
    rawasciistring = rawascii.get()

    ##getting the dimensions of the raw ascii, returns height and width
#    for character in strinng:
#        if character =="x":
#            width = strinng[:strinng.index(character)]
#            height = strinng[strinng.index(character)+1:len(strinng) ]
#            try:
#                print(width, height)
#                widthrawascii = int(width)
#                heightrawascii = int(height)
#            except ValueError:
#                processedascii.set("you have to enter two numbers for the width and the height")
#            break
#        else:
#            if strinng.index(character)+1 == len(strinng):
#                processedascii.set("you have to seperate you values by 'x'")

    widthrawascii = int(strinng)
    heightrawascii = int(len(rawasciistring)/widthrawascii)
    
    lines = []

    message=""
    startingpoint = 0
   

    for linenumber in range(heightrawascii):
        line = rawasciistring[startingpoint: (linenumber+1) *widthrawascii]
        startingpoint = (linenumber+1) * widthrawascii
        message +='"'
        message += line
        message +='",'
        message += "\n"

    processedascii.set(message)
    print(message)

    path = r"G:\Meine Ablage\USBStick\programming\dashboardascii"
    nameoffile =  os.path.join(path, filename.get())
    print(nameoffile)
    file = open(nameoffile, "w", encoding="utf-8")
    file.write(message)



#==================================================================        




rawasciientry = ttk.Entry(root,width = 50, textvariable = rawascii)
dimensionentry = ttk.Entry(root, width = 10, textvariable = dimensions)
dimensionentry.focus()
filenameentry = ttk.Entry(root, width = 30, textvariable = filename)
button = ttk.Button(root,text = "convert", command = buttonclicked)



showing_proccessedascii = ttk.Label(root,textvariable = processedascii)




dimensionentry.pack()
rawasciientry.pack()
filenameentry.pack()
button.pack()

showing_proccessedascii.pack()

root.mainloop()


