import sqlite3
from sqlite3 import Connection

def get_connection(db_name: str = "orders.db") -> Connection:
    return sqlite3.connect(db_name)


def create_tables(db_name: str = "orders.db"):

    conn = get_connection(db_name)
    cur=conn.cursor()
    cur.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Orders (
            ID INTEGER PRIMARY KEY,
            Name TEXT,
            Status TEXT,
            Price INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Operator (
            ID INTEGER PRIMARY KEY,
            Cleint_Address TEXT,
            Order_Status TEXT,
            Courier_ID INTEGER,
            Cleint_Details TEXT,
            Courier_Details TEXT,
            Order_ID INTEGER,
            FOREIGN KEY(Cleint_Address) REFERENCES Cleint(Address) ON UPDATE CASCADE,
            FOREIGN KEY(Order_Status) REFERENCES Orders(Status) ON UPDATE CASCADE,
            FOREIGN KEY(Courier_ID) REFERENCES Courier(ID) ON UPDATE CASCADE,
            FOREIGN KEY(Cleint_Details) REFERENCES Cleint(Details) ON UPDATE CASCADE,
            FOREIGN KEY(Courier_Details) REFERENCES Courier(Details) ON UPDATE CASCADE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courier (
            ID INTEGER PRIMARY KEY,
            Details TEXT,
            Order_ID INTEGER,
            Address_Cleint TEXT,
            Order_Status TEXT,
            Cleint_Details TEXT,
            FOREIGN KEY(Order_ID) REFERENCES Operator(Order_ID),
            FOREIGN KEY(Address_Cleint) REFERENCES Operator(Cleint_Address),
            FOREIGN KEY(Order_Status) REFERENCES Orders(Status),
            FOREIGN KEY(Cleint_Details) REFERENCES Operator(Cleint_Details)
        )
''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cleint (
            ID INTEGER PRIMARY KEY,
            Details TEXT,
            Address TEXT,
            Order_Status TEXT,
            Courier_Details TEXT,
            Order_Name TEXT,
            Order_ID INTEGER,
            FOREIGN KEY(Order_Status) REFERENCES Orders(Status),
            FOREIGN KEY(Courier_Details) REFERENCES Operator(Courier_Details),
            FOREIGN KEY(Order_Name) REFERENCES Orders(Name),
            FOREIGN KEY(Order_ID) REFERENCES Orders(ID)
        )
''')

    conn.commit()
    conn.close()


def insert_sample_data(db_name: str = "orders.db"):

    conn = get_connection(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Orders")
    if cursor.fetchone()[0] == 0:
        orders = [
            ("Ноутбук Acer Aspire 3u46", 16000, 1, 'На складе'),
            ("Книга Преступление и наказание", 700, 2, 'На складе'),
            ("Смартфон Samsung Galaxy S25 Ultra", 84000, 3, 'На складе')
        ]
        cursor.executemany('INSERT INTO Orders (Name, Price, ID, Status) VALUES (?, ?, ?, ?)', orders)
        print("Добавлены товары.")
        cleint=['sdfsdf','sdfsdfsdf']
        cursor.execute('INSERT INTO Cleint (Address, Details) VALUES (?, ?)', cleint)
        cursor.execute('INSERT INTO Operator (ID) VALUES (?)', (1,))
        cursor.execute('INSERT INTO Courier (ID) VALUES (?)', (1,))
    conn.commit()
    conn.close()