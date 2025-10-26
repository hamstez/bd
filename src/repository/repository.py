import sqlite3
from src.models.models import Order, Cleint, Operator

class Repository:
    def __init__(self, db_file: str = "orders.db"):
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def get_cleint(self):
        self.cursor.execute("SELECT Details, Address, Order_Status, Order_Name, Order_ID FROM Cleint WHERE ID = 1")
        row = self.cursor.fetchone()
        return Cleint(address=row["Address"], details=row["Details"], order_status=row["Order_Status"], order_name=row["Order_Name"])
    
    def get_order(self, order_id: int):
        self.cursor.execute("SELECT ID, Name, Status, Price FROM Orders WHERE ID = ?", (order_id,))
        row = self.cursor.fetchone()
        return Order(id=row["ID"], name=row["Name"], status=row["Status"], price=row["Price"])

    def update_order_status(self, order_id: int, status: str):
        self.cursor.execute("UPDATE Order SET Status = ? WHERE ID = ?", (status, order_id))
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
        self.cursor.execute("SELECT Cleint_Address, Cleint_Details, ID, Order_Status, Courier_ID, Order_ID, Courier_Details FROM Operator WHERE ID = 1")
        row=self.cursor.fetchone()
        return Operator(cleint_address=row["Cleint_Address"], cleint_details=row["Cleint_Details"], courier_id=row["Courier_ID"], id=row["ID"], order_id=row["Order_ID"], order_status=row["Order_Status"], courier_details=row["Courier_Details"])
    
    def make_order(self, id: int, ):
        self.cursor.execute('UPDATE Orders SET Status = ? WHERE ID = ?', ('Заказано', id))
        return None
    
    def give_courier_task(self, id: int):
        self.cursor.execute("UPDATE Courier SET Address_Cleint = (SELECT Address FROM Cleint WHERE ID = 1)")
        self.cursor.execute("UPDATE Courier SET Cleint_Details = (SELECT Details FROM Cleint WHERE ID = 1)")
        self.cursor.execute('UPDATE Courier SET Order_ID = ? WHERE ID = 1', (id,))
        self.cursor.execute('UPDATE Orders SET Status = ? WHERE ID = ?', ("Передано курьеру", id))
        return None

    def close(self):
        self.conn.commit()
        self.conn.close()