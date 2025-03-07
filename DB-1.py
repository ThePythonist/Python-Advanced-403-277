import sqlite3

conn = sqlite3.connect("info.db")
cur = conn.cursor()

# creating a table
# query = "CREATE TABLE cities (name,country,language);"
# cur.execute(query)

# inserting a record in a table
# query = "INSERT INTO cities VALUES ('tehran','iran','farsi');"
# cur.execute(query)

# selecting all rows from a table
query = "SELECT * FROM cities;"
cur.execute(query)

record = cur.fetchall()  # return a list of tuples
print(record)

conn.commit()
conn.close()
