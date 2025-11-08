import sqlite3
from sqlite3 import Connection

def get_connection(db_name: str = "orders.db") -> Connection:
    return sqlite3.connect(db_name)


def create_tables(db_name: str = "orders.db"):

    conn = get_connection(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            ID INTEGER PRIMARY KEY,
            Name TEXT,
            Status TEXT,
            Price INTEGER,
            Courier_ID INTEGER,
            FOREIGN KEY(Courier_ID) REFERENCES Courier(ID)
        )
''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Operator (
            ID INTEGER PRIMARY KEY,
            Courier_ID INTEGER,
            Order_ID INTEGER,
            Cleint_ID INTEGER,
            FOREIGN KEY(Cleint_ID) REFERENCES Cleint(ID),
            FOREIGN KEY(Order_ID) REFERENCES Orders(ID),
            FOREIGN KEY(Courier_ID) REFERENCES Courier(ID)
        )
''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courier (
            ID INTEGER PRIMARY KEY,
            Details TEXT,
            Order_ID INTEGER,
            Cleint_ID INTEGER,
            Operator_ID INTEGER,
            Status TEXT,
            FOREIGN KEY(Order_ID) REFERENCES Orders(ID),
            FOREIGN KEY(Cleint_ID) REFERENCES Cleint(ID),
            FOREIGN KEY(Operator_ID) REFERENCES Operator(ID)
        )
''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cleint (
            ID INTEGER PRIMARY KEY,
            Details TEXT,
            Address TEXT,
            Order_ID INTEGER,
            Courier_ID INTEGER,
            FOREIGN KEY(Courier_ID) REFERENCES Courier(ID),
            FOREIGN KEY(Order_ID) REFERENCES Orders(ID)
        )
''')

    conn.commit()
    conn.close()


def insert_data(db_name: str = "orders.db"):

    conn = get_connection(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Orders")
    if cursor.fetchone()[0] == 0:
        orders = [
            ("Ноутбук Acer Aspire 3u46", 16000, 1, 'На складе'),
            ("Смартфон Apple iPhone 14 Pro", 52999, 2, 'На складе'),
            ("Смартфон Samsung Galaxy S25 Ultra", 84000, 3, 'На складе')
        ]
        couriers = [
            (1, "+79875572173", "Свободен"),
            (2, "+79105438510", "Свободен"),
            (3, "+79295640247", "Свободен")
        ]
        cursor.executemany('INSERT INTO Orders (Name, Price, ID, Status) VALUES (?, ?, ?, ?)', orders)
        print("Добавлены товары.")
        cleint=['sdfsdf','sdfsdfsdf']
        cursor.execute('INSERT INTO Cleint (Address, Details) VALUES (?, ?)', cleint)
        cursor.execute('INSERT INTO Operator (ID) VALUES (?)', (1,))
        cursor.executemany('INSERT INTO Courier (ID, Details, Status) VALUES (?, ?, ?)', couriers)
    conn.commit()
    conn.close()