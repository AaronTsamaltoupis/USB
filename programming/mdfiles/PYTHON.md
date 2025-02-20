[packages](##packages)
[virtual environments](##virtual environments)

[loops](##loops)

[functions](##functions)
[classes](##classes)
    [constructors](##constructors)
[dictionary](##dictionary)
    [.get() method](##get_method)
[strings](##Strings)
    [printing only parts of the string](###printing parts of the string)
   [adding variables to strings](###adding variables to strings)
   [finding specific words in strings](##find() method))
[lists](##lists)
    [check if list is contained in other list](###check if list is contained in other list)
    [get position of element in list](###get position of element in list)
    [check if object is in list](##check if object is in list)
    [turning lists around](##turning lists around)
    [create list with small increments](##create list with small increments)
[tuples](##Tuples)
    [tuple unpacking](###Tuple unpacking)
[built in functions](##built in functions)
[File Input and Output](##File Input and Output)
    [writing text files](###writing files)
    [reading txt files](###reading txt files)
    [appending to text files](###appending to files)
    [complicated folder structures](### complicated folder structures)
    [the os module](###the os module)
    [the glob module](###the glob module)

    [csv files](##csv files)
      [reading csv files](##reading csv files)       
      [writing csv files](##writing csv files)
    [pdffiles](##pdffiles)

[exeptions](##exeptions)
[packages](##packages)
   [random](##random)    
   [math module](##math_module)
    [numpy](#numpy)
    [pyplot](##pyplot)
    [matplotlib](##matplotlib)
    [tkinter](##tkinter)
     -[Root](##Root)  
     -[ttk](##ttk)
     -[the StringVar object](###the StringVar object)
     -[Entry](##Entry)        
     -[Button](##Button)        
     -[Label](##Label)        
     -[input boxes](###input boxes)

[interacting with the web](##inter acting with the web)


[##virtual](##virtual) environments
self contained location for isolated environments for python projects
-manages packages without conflicts
-packages are installed in an isolated location for one project
-each project has its own unique set of packages

venvs are direcories containing the packages

###exporting packages
pip freeze > requirements.txt

###importing packages from other environment
pip install -r requirements.txt


creating venv:
-navigate to project folder

##create venv:
windows: python -m venv env(name of venv)
linux: python3 -m venv env(name of venv)

activate venv:
windows: nameofvenv/Sripts/activate.bat
linux: source nameofvenv/bin/activate

 -only if the venv is activated can code be interpreted with the packages in the venv

deactivating venv: 
deactivate

list all packages in environment:
   pip list

installing packages in venv:
 pip install packagename



##loops
break

for i in range(4):
  if i ==2:
   break
  print(i)

print("helo")

when i hits 2 the entire loop is aborted and the code jumps to after the loop

continue

for i in range(4):
  if i ==2:
   continue
  print(i)

print("hello")

when i hits 2 the current run of the loop is aborted but the loop still does the remaining repititions just skipping the rest of the 2 repition (2 is never printed)


##functions



##classes
classes are new types of object defined by the user
the classes are first defined, then objects can be assigned the type of the function:
they then inhabit every method defined in the class 

class Point:
    <> #all functions (methods) of the class are defined here
    def move(self):
        print("move"

point1 = Point()

object:
instance of a class, the actual objects that use the type defined in the class
point1 in this case is an object of the type Point with all methods defined in Point

point1.move

different values (attributes) can be assigned to object:

point1.x = 10
print(point2.x)

if there is a different object of the same type poin2 = Point() it does not have any of the attributes defined for the other points, they need to be defined first

if an attribute is called without being defined first an AttributeError is returned

##constructors
to make sure every object of a type has certain attributes constructors can be used

constructors are functions(methods) from the callthat are called immediately when creating the obejct
the arguments for those functions are provided when calling the obejct
this special function defined in the class is the __init__ function (initialize)
the actual arguments used in the initialize function are given after the self argument
the self argument references the new object that is being created:
that means the code self.x in the function is the same as object.x when object = Point() if the function was called manually:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

the self argument can also be referenced in other not initialize functions defined in the class
this way other methods defined earlier in the class can be used in later methods, bspw:

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi, I am {self.name}")

##Inheritance





##importing modules
from module import *

##dictionary
store information that come as value pairs

dictionary = {
    "categoryname1": value1
    "categoryname2": vale2
}

dictionary["categoryname1"]

        -returns value assigned to categoryname1

to each categoryname there is assigned a value similar to a function
no categoryname can have two values, therefore: every categoryname must be unique

new categories can be added to the dictionary afterwards:
directory["newcategory"] = value

delete key:
 del(dectionary[categoryname])

 listing all keys of a dictionary:
 dictionary.keys()
 .keys() returns no list even if it looks like it
 type(dictionary.keys())
   returns dict_keys    

for key in dictionary:
  code

loops through every key in a dictionary


check whether variable in dictionary:
variable in dictionary
  checks whether "variable" is a key in "dictionary"kk  



###get_method
dictionary.get("categoryname")
    -also returns value assigned to categoryname but returns None if categoryname doesn't exist in the dictionary
dictionary.get("categoryname", "error")
    -returns "error" whenever categoryname doesn't exist


##Strings

###printing parts of the string
line = "hello world"
lines_piece = line[1:3]

lines_piece="el"

returns:
line = "hello world"
lines_piece = line[0:(len(line)-3)]
    -removes three characters from original line

###adding variables to strings
f'string{variable}continued string'


##find() method
stringexample  = "this is a string"
stringexample.find("his") finds first occurrence of  "his"" inside stringexample" and returns index of first character of "his"


##lists
###check if list is contained in other list
list1 = [1,2,3,4,5]
list2 = [1,2,3]

set(list1).issubset(set(list2))
-returns true if list1 is a subset of list2


###get position of element in list
list.index(element)
    -returns the index of the element in the list
    -returns value error if element not in the list
    
###check if object is in list
object in list
    -returns boolean value
###create list with small increments
import numpy as np

list = np.arange(float(startingpoint), float(endpoint), increment).tolist()

##Tuples

### Tuple unpacking
list-of-tuples = [(a1, b1, b2), (a2, b2, b3), ......]

for (a, b, c) in list-of-tuples:
    print(a)
    print(b)
    print(c)
    
-splits every tuple in its components and returns them seperately


other way:
tuple = (a1, a2, a3)
x, y, z = tuple
assigns x to a1, y to a2, z to a3

##built in functions
type(object)
    -returns type of an object:
    types:
        -str
        -int
        -type








## File Input and Output
open() function:
needs to arguments:	1. the file name
			2. whether to [read](###reading files) from the file or to [write](###writing files) in the file
bsp: 
myOutpuFile = open("hello.txt", "w")
 this creates a new file called hello.txt, unless specified otherwise it  is created in the same folder as the script
 
myOutputFile.close()
 this closes the function


 opening file without needing to close it:

 with open(filename, "mode") as myFile:
  -operations on file     

bspw: 
with open(os.path.join(myPath, "test.txt"), "r") as myfile:
    for line in myfile.readlines():
        print(line, end = "")


 
opening a file stored somewhere else:
myInputFile = open(r"C:\path\to\file.txt")

[the os module](###the os module)
### writing files
# if an already existing file is opened in write mode its content is deleted
	to add lines see [append mode](###appending to files)

myOutputFile = open("hello.txt", "w")
myOutputFile.writelines("this is my first file.")
myOutpuFile.close()


writing several lines:
lines can be stored in a list, linebreaks need to be specified by \n:

linesToWrite = ["this is line1", "\n this is line2", "\n this is line3]
myOutputFile.writelines(linesTowrite)


reading from a file stored somewhere else:
myInputFile = open(r"C:\path\to\file.txt", "w")




### appending to files
linebreaks need to be specified even on the first line:
bsp
myOutputFile= open('file.txt', 'a')
linesToAdd = ["\nThis is an added line"]
myOutpuFile.writelines(linesToAdd)
myOutputFile.close()



### reading txt files
myInputfile = open("hello.txt", "r")
print myInputfile.readlines()
myInputfile.close()

printing each line seperately:

myInputFile = open("Julia.md", "r")

for x in myInputFile.readlines():
    print(x,  end = "")
    
myInputFile.close()


the end = "" part has to be added, otherwise the print function adds extra linebreaks
anything can be added in the end section, python will print this at the start of each line starting with the second one

### complicated folder structures
import os

myPath = r"C:\Users\User\Desktop\Notes"
inputFileName = os.path.join(myPath, "Julia.md")
with open(inputFileName, "r")as myInputFile:
    for line in myInputFile.readlines():
        print(line, end="")

os.path.join() function combines to paths to create a single  valid path





### the os module
gives some of thesame basic functions as a terminal (bspw to make or delete directories)

functions:
os.path.join(path1, path2)
    -joins two path strings into a valid path
os.listdir(path/to/directory)
    -creates a list of every file and folder in the directory (but not the files in the folders)
os.rename(path/to/file_oldname, path/to/file_newname)
os.path.isfile(path/to/object)
    -checks if the object is a file, returns boolean
os.path.isdir(path/to/object)
    -checks if the object is a directory, returns boolean
os.path.exists(path/to/object)
    -checks if file exists, returns True if it exists
os.walk(path/to/directory)
    -returns list of tuples of the form: (directory, [subfolders], [files]) for each directory
    -for each subfolder of the directory the tuple contains: (path/to/directory, [list of subfolders in directory], [list of files in the directory(not in subfolders)])
    -this is reapeated for each subfolder, even those already listed in the subfolders category of previous tuples
os.path.getsize(path/to/file)
    -returns integer of the size of the file in bites
os.path.remove(path/to/file)
    -deletes file

    
modules:
filename.endswith(.extension)
    -returns boolean value:
    True if filename has .extension extension, False if not


example of functions:		(keyword: removing characters from a string)
rename every .gif file in a folder to be a.jpg file
import os

path = r"C:\Users\User\Desktop\aaron"

fileNameslist = os.listdir(path)
for file in fileNameslist:
    if file.endswith(".md"):
        new_filename = (file[0:len(file)-2] + "txt")
        os.rename(os.path.join(path, file), os.path.join(path, new_filename))


print(os.listdir(path))


###the glob module
functions:
glob.glob(path\to\directory\*.extension): creates a list: filters a directory for a given filetype (fileextension)
takes directory with * and an extension as the argument
* in this case stands for "any": the list should contain any file in the directory with the file extension .extension
creates a list of all files in the given directory with that extension
glob.glob(path\to\directory\*\*.extension)
looks for file extensions only in files that are in folders in the directory (one layer deeper)
the filtered files can be further specified: "image[0-9][0-9].gif" searches for any .gif file that is called "image" followed by to numbers in the range 0-9
        * is not used here as we are not filtering for any file but only files with a specific file name

    
   
   
##csv files
csv: comma seperated value

the first line of the csv file is the header assigning names to the rows of data, thereby telling what each entry represents

the entries in each line have to appear in the same order to match with the header

csv module
import csv, makes it easy to read and write csv files


##reading csv files
with open(filename, "r") as myFile:
 myFileReader = csv.reader(myFile)
 for rown in myFileReader:
  print(row)  

to read a csv file the opened file first has to be passed to the csv.reader()
single rows of data in csv reader are displayed as lists

these list can be unpacked like this:

for headerentry1, headerentry2, ... in myFileReader:
  print(headerentry1, headerentry2)  

sometimes csv use different delimiters than commas:
delimiter can be specified when reading file e.g. entries are seperated by tabs:
myFileReader = csv.reader(openedfile, delimiter = "/t")

skipping rows in the File Reader:
myFileReader = csv.reader(myfile)
next(myFileReader)
skips the next file in the reader
the reader remembers where it left off

bspw: 
myFileReader = csv.reader(myfile)
next(myFileReader)
for row in myFileReader:
  print(row)  

      skips the first row (header)


##writing csv files
myFile = open(filepath, "w")
myFileReader = csv.writer(myFile)
myFileReader.writerow(["Movie", "Rating"])
myFileREader.writerow(["Chihiros Reise ins Zauberland", 4])

myFile.close()

write several rows at once:
rows = [["movie", "rating"], ["chihiros reise ins zauberland", 4], ["the circle", 0]]

myFile = open(filepath, "w")
myFileReader = csv.writer(myFile)
myFileReader.writerow(["Movie", "Rating"])
myFileREader.writerow(["Chihiros Reise ins Zauberland", 4])

myFile.close()


##pdffiles
import pypdf





##sql database
general:
data is stored in a series of tables with unique names
 each column in the tables also is given a unique name (similar to the header giving each row a unique name in csv files)
 each column has to have a unique name for its table (names cannot have spaces, special characters etc)

 Primary key:
 column in a table used for indexing the table
 this column has to have guaranteed unique entries for each row bspw using a unique id for each row

relating the information in different tables:
relational database:

two different tables can be linked by a third table

bspw [linkingnewslettersubscriptions.md](linkingnewslettersubscriptions.md)


sql in python

import sqlite3
connection = sqlite3.connect("test_database.db")

     --sqlite3 is connected to the database file

c = connection.cursor
     --creates cursor object where methods on the database can be executed

methods:
a.execute("CREATE TABLE NameofTable(Key1 TEXT, Key2 TEXT, Key3 INT)")
bspw: 
a.execute("CREATE TABLE People(FirstName TEXT, Lastname TEXT, Age INT)")

the types of the values of the Keys have to be specified: TEXT, INT

c.execute("INSERT INTO People VALUES ('Angela', 'Merkel', 70)")
connection.commit()
    -neccessary to actually save changes to the table
    -ACHUTUNG: quotation marks around TEXT VALUES have to be 'Angela' not "Angela"

deleting table:
c.execute("DROP THE TABLE IF IT EXISTS NameofTable")

simplify opening of databases:
with sqlite3.connect("test_database.db") as connection:
  c = connection.cursos
  c.execute(< >)

-changes now don't have to be commited



##packages
installing packages systemwide: 
arch linux: sudo pacman -S python-numpy


##random
randint(x, y)
 -returns random integer between x and y, including x and y
random()
 -returns random value between 0 and 1





##math_module
math.floor(5.6)
returns 5
floor method rundet ab
math.floor(-23.11) :  -24.0

math.ceiling(5.6)
returns 6
rundet auf



##exeptions
try:
    code
except SpecificError:
    alternative code
        
    
##packages

##numpy
import numpy as np
np.array()
type : <class 'numpy.ndarray'>
takes one argument

0 dimensional:
np.array(40)
    -cannot iterate over 0 dimensional array
onedimensional: 
np.array([1,2,3])
    -only takes one list or tuple as an argument, returns a onedimensional array
multidimensional:
    -takes list of lower dimensional arrays as arguument
2d
np.array([[1, 2, 3], [2, 3, 4]])
    [1, 2, 3] and [2, 3, 4] are onedimensional arrays
3d
np.array([[[1, 2, 3],[ 2, 3, 4]], [[2, 3, 4],[4, 5, 6]]])
...

###check dimensions of array
a = np.array(list)
a.ndim


the array object:
faster than traditional python list
returned array object looks similar to list, just without commas 

=========================================
##pyplot


##matplotlib
plot() function:
-takes two arguments: one array for x axis, one array for y axis








##Tkinter
tkinter is not a pip package:
 sudo pacman -S tk

import tkinter as tk

##Root
root = tk.Tk()
--
--
root.mainloop()
 -creates new tkinter window and assigns it name root

###labeling the window:
root.title("title of window")

###changing size of window:
root.geometry("800x600")

###changing the icon of the window
root.iconbitmap(r"G:\Meine Ablage\USBStick\programming\luigimangione.ico")
 the file has to be a .ico file


##ttk
-more modern designs of windows

import tkinter as tk
from tkinter import ttk

###the StringVar object
helps to manage values of widgets that can have values (bspw entries, labels)
 





##Entry
entrybox = ttk.Entry(root,  width = 50)

have the cursor in the entry box when opening the window:
entrybox.focus()
 

use inserted text in entry box as variable:

  typedtext = tk.StringVar()
  entrybox = ttk.Entry(root,  width = 50, textvariable = typedtext)
  entrybox.pack()

  button = ttk.Button(root, command = button_pressed)

   (the button_pressed() function defined earlier then calls the value of the typedtext.get() method)    

it is important that the value of the stringVar variable is called with get() only after everything is written and a new action is performed (e.g. pressing the button)

step by step progress: 

--first create string variables that hold the updated text in the entries:
text1 = tk.StringVar()
text2 = tk.StringVar()

--then for each string variable create a corresponding entry widget
text1entry = ttk.Entry(root,textvariable = text1)
text2entry = ttk.Entry(root,textvariable = text2)




##Button
def buttonclicked():
 function

button = ttk.Button(root, command = buttonclicked)












##inter acting with the web
##webscraping



static route


flask
from flask import Flask



app = Flask(__name__) ## 

@app.route("/")
@app.route("/<>")

##this sets the url of the page, which in this case would be http://localhost:5000/hello

def hello_world():
    return("hellllllo world")


if __name__ == "__main__":
    app.run()



dynamic route:

change @app.route to :

@app.route("/tesst/<search_query>")
-the url of the webpage is now tesst/ followed by whatever the user enters which is saved as the variable <search_query>

if this variable is incorporated into a function it can be printed on the page:

def search():
 return(search_query)

each value that is returned to the webpage is actually a tuple consisting of 





