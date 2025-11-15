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
            Client_ID INTEGER,
            FOREIGN KEY(Client_ID) REFERENCES Client(ID),
            FOREIGN KEY(Order_ID) REFERENCES Orders(ID),
            FOREIGN KEY(Courier_ID) REFERENCES Courier(ID)
        )
''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courier (
            ID INTEGER PRIMARY KEY,
            Details TEXT,
            Order_ID INTEGER,
            Client_ID INTEGER,
            Operator_ID INTEGER,
            Status TEXT,
            Password INTEGER,
            FOREIGN KEY(Order_ID) REFERENCES Orders(ID),
            FOREIGN KEY(Client_ID) REFERENCES Client(ID),
            FOREIGN KEY(Operator_ID) REFERENCES Operator(ID)
        )
''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Client (
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
            ("Смартфон Samsung Galaxy S25 Ultra", 84000, 3, 'На складе'),
            ("Планшет Apple iPad Pro 13 M5", 109999, 4, 'На складе'),
            ("Фотокамера Sony Alpha A6000", 45999, 5, 'На складе')
        ]
        couriers = [
            (1, "+79875572173", "Свободен", 123123),
            (2, "+79105438510", "Свободен", 234234),
            (3, "+79295640247", "Свободен", 345345)
        ]
        cursor.executemany('INSERT INTO Orders (Name, Price, ID, Status) VALUES (?, ?, ?, ?)', orders)
        print("Добавлены товары.")
        client=['sdfsdf','sdfsdfsdf']
        cursor.execute('INSERT INTO Client (Address, Details) VALUES (?, ?)', client)
        cursor.execute('INSERT INTO Operator (ID) VALUES (?)', (1,))
        cursor.executemany('INSERT INTO Courier (ID, Details, Status, Password) VALUES (?, ?, ?, ?)', couriers)
    conn.commit()
    conn.close()