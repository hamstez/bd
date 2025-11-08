import sqlite3
from src.models.models import Order, Cleint, Operator, Courier

class Repository:
    def __init__(self, db_file: str = "orders.db"):
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def get_cleint(self):
        self.cursor.execute("SELECT ID, Details, Address, Order_ID, Courier_ID FROM Cleint WHERE ID = 1")
        row = self.cursor.fetchone()
        return Cleint(id=row["ID"], address=row["Address"], details=row["Details"], order_id=row["Order_ID"], courier_id=row["Courier_ID"])
    
    def get_order(self, order_id: int):
        self.cursor.execute("SELECT ID, Name, Status, Price FROM Orders WHERE ID = ?", (order_id,))
        row = self.cursor.fetchone()
        return Order(id=row["ID"], name=row["Name"], status=row["Status"], price=row["Price"])
    
    def get_courier(self):
        self.cursor.execute("SELECT ID, Details, Order_ID, Cleint_ID, Operator_ID FROM Courier WHERE ID = 1")
        row = self.cursor.fetchone()
        return Courier(id=row["ID"], details=row["Details"], order_id=row["Order_ID"], cleint_id=row["Cleint_ID"], operator_id=row["Operator_ID"])

    def update_order_status(self, order_id: int, status: str):
        self.cursor.execute("UPDATE Orders SET Status = ? WHERE ID = ?", (status, order_id))
        return None
    
    def get_all_orders(self):
        self.cursor.execute("SELECT ID, Name, Status, Price FROM Orders")
        rows = self.cursor.fetchall()
        return [Order(id=row["ID"], name=row["Name"], status=row["Status"], price=row['Price']) for row in rows]
    
    def update_cleint_details(self, details: str):
        self.cursor.execute('UPDATE Cleint SET Details = ? WHERE ID = 1', (details,))
        return None
    
    def update_cleint_address(self, address: str):
        self.cursor.execute('UPDATE Cleint SET Address = ? WHERE ID = 1', (address,))
        return None
    
    def get_operator(self):
        self.cursor.execute("SELECT ID, Courier_ID, Order_ID, FROM Operator WHERE ID = 1")
        row=self.cursor.fetchone()
        return Operator(courier_id=row["Courier_ID"], id=row["ID"], order_id=row["Order_ID"], cleint_id=row["Cleint_ID"])
    
    def make_order(self, id: int):
        self.cursor.execute('UPDATE Orders SET Status = ? WHERE ID = ?', ('Заказано', id))
        return None
    
    def update_courier_task(self, id: int):
        self.cursor.execute('UPDATE Orders SET Status = ? WHERE ID = ?', ("Передано курьеру", id))
        return None

    def get_new_order(self):
        self.cursor.execute("SELECT ID, Name, Status, Price FROM Orders WHERE Status = ?", ("Заказано",))
        rows = self.cursor.fetchall()
        return [Order(id=row["ID"], name=row["Name"], status=row["Status"], price=row['Price']) for row in rows]

    def close(self):
        self.conn.commit()
        self.conn.close()