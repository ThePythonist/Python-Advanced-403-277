import sqlite3

students = [
    {"name": "kiana", "major": "computer science", "grade": 17.5},
    {"name": "mohamad", "major": "motarjemi almani", "grade": 19.8},
    {"name": "samyar", "major": "electrical engineering", "grade": 14.23},
    {"name": "reyhane", "major": "architecture", "grade": 16.93},
]


def create():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE students (name,major,grade);")
    print("Successfully created table students")
    conn.commit()
    conn.close()


def insert(student):
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = f"INSERT INTO students VALUES {(student['name'], student['major'], student['grade'])}"
    cur.execute(query)

    print(f"Successfully inserted {student['name']}")
    conn.commit()
    conn.close()


# create()
for i in students:
    insert(i)
