import numpy as np
import tkinter as tk
import csv
import os

myPath = "/home/aaron/Desktop/USB/programming/datafiles"


with open(os.path.join(myPath, "customers-100.csv"), "r") as myfile:
    myFileReader = csv.reader(myfile)
    next(myFileReader)
    for Index,CustomerId,FirstName,LastName,Company,City,Country,Phone1,Phone2,Email,SubscriptionDate,Website in myFileReader:
        print(f' {FirstName} {LastName} living in {City}')
