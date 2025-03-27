import sqlite3


def createTable():
    name = input("Enter table name : ")
    columns = tuple(input("Enter table columns (separated by comma) : ").split(","))

    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = f"CREATE TABLE IF NOT EXISTS {name} {columns};"
    cur.execute(query)

    conn.commit()
    conn.close()

    print(f"Successfully created table {name}")


def insertRecord():
    name = input("Enter table name : ")

    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = f"PRAGMA table_info({name});"
    cur.execute(query)

    columns = [i[1] for i in cur.fetchall()]
    values = []

    for i in columns:
        values.append(input(f"Enter {i} : "))

    query = f"INSERT INTO {name} VALUES {tuple(values)};"
    cur.execute(query)

    conn.commit()
    conn.close()

    print("Successfully inserted record")


def selectTable():
    # TODO : handle filtering for select

    name = input("Enter table name : ")

    conn = sqlite3.connect("info.db")
    cur = conn.cursor()

    query = f"SELECT * FROM {name};"
    cur.execute(query)

    records = cur.fetchall()

    if len(records) == 0:
        print("No data is available in this table")
        return

    for i in records:
        print(i)

    conn.commit()
    conn.close()


def main():
    choice = input("""
1 : Create a table
2 : Insert into a table
3 : Show a table
Choice : """)

    if choice == "1":
        createTable()
    elif choice == "2":
        insertRecord()
    elif choice == "3":
        selectTable()
    else:
        print("Invalid option, Try again.")
        main()


main()
