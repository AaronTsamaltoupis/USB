
[##creating a new table:](##creating a new table)
[##insert into existing table](##insert into existing table)



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

steps for working with databases:
create connection with database
create a cursor for the connection
execute sql query`


import sqlite3
connection = sqlite3.connect("test_database.db")
     --create a new database        
     --sqlite3 is connected to the database file

c = connection.cursor
     --creates cursor object where methods on the database can be executed

connection.close()
    --closes connection to database



methods:
##creating a new table:
c.execute("CREATE TABLE NameofTable(Key1 TEXT, Key2 TEXT, Key3 INT)")
bspw: 
c.execute("CREATE TABLE People(FirstName TEXT, Lastname TEXT, Age INT)")

the types of the values of the Keys have to be specified: TEXT, INT

create table for short time:
connection = sqlite3.connect(":memory")
 -database disappears when connection is closed







##insert into existing table
c.execute("INSERT INTO People VALUES ('Angela', 'Merkel', 70)")
connection.commit()
    -neccessary to actually save changes to the table
    -ACHUTUNG: quotation marks around TEXT VALUES have to be 'Angela' not "Angela"

deleting table:
c.execute("DROP THE TABLE IF IT EXISTS NameofTable")

simplify opening of databases:
with sqlite3.connect("test_database.db") as connection:
  c = connection.cursor()
  c.execute(< >)

-changes now don't have to be commited

##execute several sql statements:
bspw insert many rows of values at once using tuples:

with  sqlite3.connect("citypopulation.db")as connection:
  cursor = connection.cursor()
  cities = [('Berlin', 'Deutschland', 3200000), ('Paris', 'Frankreich', 2100000)]
  cursor.executemany('INSERT INTO citypopulation VALUES (?,?,?)', cities)


  the ? act as placeholders (paramterized statements) for the keys in the table 




#Importing data from a csv file

import csv

csv.reader(open(file.csv)) returns a list of tuples it can therefore be added to a table using the executemany method


#retreiving data from sql database table
cursor.execute("SELECT key1, key2, from tablename")

returns an object that can be iterated over:

for row in cursor.execute("SELECT key1, key2, FROM tablename"):
  print(row)

--returns rows as tuples of the values for key1 and key2

cursor.execute("SELECT * FROM tablename")
--selects everything  

cursor.fetchall() returns a list of a tuple containing the values of all selected keys:

cursor.execute("SELECT key1, key2 from tablename")

cursor.fetchall()
returns: [(firstrow1,firstrow2), (secondrow1, secondrow2), ...]


#selecting specific records:

cursor.execute("SELECT * FROM tablename WHERE keya = (?)", (parameter,))

-selects all records where keya takes the value of the parameter




#changing records in database:

cursor.execute("UPDATE customer SET keya = newvalue WHERE keyb = valueb")

keyb and valueb are used to identify the row in which the value of keya should be changed.


#deleting records in database:
cursor.execute("DELE FROM tablename WHERE keyb = valueb")

deletes all rows for which keya takes the value valuea


#joining data from multiple tables




