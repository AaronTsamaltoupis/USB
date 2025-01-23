import numpy as np

connection = sqlite3.connect("text_database.db")

c = connection.cursor()

c.execute("CREATE TABLE People(FirstName TEXT, surname TEXT, Age INT)")
c.execute("INSERT INTO People VALUES ('Angela', 'Merkel', 70)")

connection.commit()
