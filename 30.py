import sqlite3


def create():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE employees (name,salary,experience);")
    print("Successfully created table employees")
    conn.commit()
    conn.close()


def insert():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO employees VALUES ('taha','5600','5');")
    cur.execute("INSERT INTO employees VALUES ('aylar','4800','2');")
    cur.execute("INSERT INTO employees VALUES ('keyvan','8000','7');")
    cur.execute("INSERT INTO employees VALUES ('lohrasb','4900','2');")
    print("Successfully inserted 4 records")
    conn.commit()
    conn.close()


# def select():
#     conn = sqlite3.connect("info.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM employees;")
#     records = cur.fetchall()
#     for i in records:
#         if int(i[1]) >= 5000:
#             print(i)
#     conn.commit()
#     conn.close()

def select():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE salary >= '5000';")
    records = cur.fetchall()
    for i in records:
        print(i)
    conn.commit()
    conn.close()


# create()
# insert()
select()
