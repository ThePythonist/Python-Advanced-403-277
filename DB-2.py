import sqlite3


def create():
    conn = sqlite3.connect("info2.db")
    cur = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    code INT,
    job VARCHAR(70)
    );
    """
    cur.execute(query)
    conn.commit()
    conn.close()


def insert(name, code, job):
    conn = sqlite3.connect("info2.db")
    cur = conn.cursor()
    query = f"INSERT INTO employees (name,code,job) VALUES {(name, code, job)}"
    # print(query)
    cur.execute(query)
    conn.commit()
    conn.close()


# insert("arman", 11501, "software engineer")
insert("ali", 11506, "electrical engineer")
