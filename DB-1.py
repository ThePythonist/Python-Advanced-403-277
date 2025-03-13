import sqlite3

conn = sqlite3.connect("info.db")
cur = conn.cursor()

# creating a table
# query = "CREATE TABLE cities (name,country,language);"
# cur.execute(query)

# inserting a record in a table
# query = "INSERT INTO cities VALUES ('tehran','iran','farsi');"
# cur.execute(query)

# deleting a specific row in a table
# query = "DELETE FROM customers WHERE phone='09118982351';"
# cur.execute(query)
# conn.commit()

# deleting all rows in a table
# query = "DELETE FROM customers;"
# cur.execute(query)
# conn.commit()

# deleting a table
# query = "DROP TABLE customers;"
# cur.execute(query)
# conn.commit()

# selecting all rows from a table
query = "SELECT * FROM customers;"
cur.execute(query)

record = cur.fetchall()  # return a list of tuples
print(record)

conn.commit()
conn.close()
