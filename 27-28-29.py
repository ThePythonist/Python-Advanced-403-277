import sqlite3


def create():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE customers (name,city,phone);")
    print("Successfully created table customers")
    conn.commit()
    conn.close()


def insert():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO customers VALUES ('taha','yazd','09196807043');")
    cur.execute("INSERT INTO customers VALUES ('aylar','tabriz','09389003158');")
    cur.execute("INSERT INTO customers VALUES ('keyvan','tehran','09118982351');")
    cur.execute("INSERT INTO customers VALUES ('lohrasb','shiraz','09020837532');")
    print("Successfully inserted 4 records")
    conn.commit()
    conn.close()


def select():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers;")
    records = cur.fetchall()
    for i in records:
        print(i[2])
    conn.commit()
    conn.close()


# create()
# insert()
select()
