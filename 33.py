import sqlite3


def check_duplicate(name, code, job):
    conn = sqlite3.connect("info2.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees;")
    records = cur.fetchall()

    for i in records:
        if i[1:] == (name, code, job):
            return True


def insert(name, code, job):
    if not check_duplicate(name, code, job):
        conn = sqlite3.connect("info2.db")
        cur = conn.cursor()
        query = f"INSERT INTO employees (name,code,job) VALUES {(name, code, job)};"
        cur.execute(query)
        conn.commit()
        conn.close()
    else:
        print("Employee already exists in db")


# check_duplicate("ali", 11506, "electrical engineer")
insert("hamed", 11506, "electrical engineer")
