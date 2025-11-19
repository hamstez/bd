import csv
import json
import sqlite3
import xml.etree.ElementTree as ET
import yaml

from src.models.models import Order, Client, Courier


class Repository:
    def __init__(self, db_file: str = "orders.db"):
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def get_client(self):
        self.cursor.execute("SELECT ID, Details, Address, Order_ID, Courier_ID FROM Client WHERE ID = 1")
        row = self.cursor.fetchone()
        return Client(id=row["ID"], address=row["Address"], details=row["Details"], order_id=row["Order_ID"], courier_id=row["Courier_ID"])
    
    def get_order(self, order_id: int):
        self.cursor.execute("SELECT ID, Name, Status, Price, Courier_ID FROM Orders WHERE ID = ?", (order_id,))
        row = self.cursor.fetchone()
        return Order(id=row["ID"], name=row["Name"], status=row["Status"], price=row["Price"], courier_id=row["Courier_ID"])
    
    def get_courier(self, id: int):
        self.cursor.execute("SELECT ID, Details, Order_ID, Client_ID, Status, Password FROM Courier WHERE ID = ?", (id,))
        row = self.cursor.fetchone()
        return Courier(id=row["ID"], details=row["Details"], status=row["Status"], order_id=row["Order_ID"], client_id=row["Client_ID"], password=row["Password"])

    def update_order_status(self, order_id: int):
        stat=["На складе", "В работе", "Отменен", "Доставлен"]
        print("\nВыберите новый статус")
        print('1 - На складе')
        print("2 - В работе")
        print('3 - Отменен')
        print('4 - Доставлен')
        try:
            status_id = int(input("\nВаш выбор: "))
        except ValueError:
            print('Ошибка ввода!')
            return 0
        if 0<status_id<5:
            self.cursor.execute("UPDATE Orders SET Status = ? WHERE ID = ?", (stat[status_id-1], order_id))
        else:
            print("\nНет такого статуса!")
        return None

    def update_courier_status(self, id: int):
        stat = ["Свободен", "Занят"]
        print("\nВыберите новый статус")
        print('1 - Свободен')
        print("2 - Занят")
        try:
            status_id = int(input("\nВаш выбор: "))
        except ValueError:
            print('Ошибка ввода!')
            return 0
        if 0<status_id<3:
            self.cursor.execute("UPDATE Courier SET Status = ? WHERE ID = ?", (stat[status_id-1],id))
        return None
    
    def get_all_orders(self):
        self.cursor.execute("SELECT ID, Name, Status, Price, Courier_ID FROM Orders")
        rows = self.cursor.fetchall()
        return [Order(id=row["ID"], name=row["Name"], status=row["Status"], price=row['Price'], courier_id=row["Courier_ID"]) for row in rows]
    
    def update_client_details(self, details: str):
        self.cursor.execute('UPDATE Client SET Details = ? WHERE ID = 1', (details,))
        return None
    
    def update_client_address(self, address: str):
        self.cursor.execute('UPDATE Client SET Address = ? WHERE ID = 1', (address,))
        return None
    
    def make_order(self, id: int):
        self.cursor.execute('UPDATE Orders SET Status = ? WHERE ID = ?', ('Заказано', id))
        return None
    
    def update_courier_task(self, id1: int, id2: int):
        self.cursor.execute('UPDATE Orders SET Status = ? WHERE ID = ?', ("Передано курьеру", id1))
        self.cursor.execute("UPDATE Courier SET Status = ? WHERE ID = ?", ("Занят", id2))
        self.cursor.execute("UPDATE Courier SET Order_ID = ? WHERE ID = ?", (id1, id2))
        self.cursor.execute("UPDATE Orders SET Courier_ID = ? WHERE ID = ?",(id2, id1))
        return None

    def get_all_o(self, id: int):
        self.cursor.execute("SELECT * FROM Orders WHERE ID = ?", (id,))
        rows=self.cursor.fetchall()
        return [Order(id=row["ID"], name=row["Name"], status=row["Status"], price=row['Price'], courier_id=row["Courier_ID"]) for row in rows]

    def get_all_c(self, id: int):
        self.cursor.execute("SELECT * FROM Courier WHERE ID = ?", (id,))
        rows=self.cursor.fetchall()
        return [Courier(id=row["ID"], details=row["Details"], order_id=row["Order_ID"], client_id=row["Client_ID"], status=row["Status"], password=row["Password"]) for row in rows]

    def get_new_order(self, id: int):
        self.cursor.execute("SELECT ID, Name, Status, Price, Courier_ID FROM Orders WHERE Courier_ID = ?", (id,))
        rows = self.cursor.fetchall()
        return [Order(id=row["ID"], name=row["Name"], status=row["Status"], price=row['Price'], courier_id=row["Courier_ID"]) for row in rows]

    def close(self):
        self.conn.commit()
        self.conn.close()

    def get_all_couriers(self):
        self.cursor.execute("SELECT ID, Details, Order_ID, Client_ID, Status, Password FROM Courier",)
        rows = self.cursor.fetchall()
        return [Courier(id=row["ID"], details=row["Details"], status=row["Status"], order_id=row["Order_ID"],
                       client_id=row["Client_ID"], password=row["Password"]) for row in rows]

    def make_json(self):
        self.cursor.execute("SELECT c.Details, c.ID, o.Name, o.Status, o.Price FROM Courier c LEFT JOIN Orders o ON c.Order_ID = o.ID WHERE c.ID IN (1, 2, 3)")
        data = []
        rows = self.cursor.fetchall()
        for row in rows:
            data.append(dict(zip([column[0] for column in self.cursor.description], row)))

        # Преобразовать данные в формат JSON с указанной кодировкой
        json_data = json.dumps(data, indent=4, ensure_ascii=False)

        # Сохраните JSON в файл с указанной кодировкой
        with open('out/output.json', 'w', encoding='utf-8') as f:
            f.write(json_data)
        return None

    def make_csv(self):
        self.cursor.execute(
            "SELECT c.Details, o.ID, o.Name, o.Status, o.Price FROM Courier c LEFT JOIN Orders o ON c.Order_ID = o.ID WHERE c.ID IN (1, 2, 3)")
        data = []
        rows = self.cursor.fetchall()
        for row in rows:
            data.append(dict(zip([column[0] for column in self.cursor.description], row)))
        columns=['Details', 'Name', 'Status', 'Price', 'ID']
        csv_writer = csv.DictWriter(open('out/output.csv', 'w', encoding='utf-8'), fieldnames=columns)
        csv_writer.writeheader()

        with open('out/output.csv', 'w', encoding='utf-8') as f:
            csv_writer.writerows(data)
        return None

    def make_xml(self):
        self.cursor.execute(
            "SELECT c.Details, c.ID, o.Name, o.Status, o.Price FROM Courier c LEFT JOIN Orders o ON c.Order_ID = o.ID WHERE c.ID IN (1, 2, 3)")
        rows = self.cursor.fetchall()
        column_names = [description[0] for description in self.cursor.description]

        root = ET.Element("data")

        for row in rows:
            row_element = ET.SubElement(root, "row")
            for i, column_name in enumerate(column_names):
                ET.SubElement(row_element, column_name).text = str(row[i])

        tree = ET.ElementTree(root)
        tree.write("out/output.xml", encoding="utf-8", xml_declaration=True)
        return None

    def make_yaml(self):
        self.cursor.execute(
            "SELECT c.Details, c.ID, o.Name, o.Status, o.Price FROM Courier c LEFT JOIN Orders o ON c.Order_ID = o.ID WHERE c.ID IN (1, 2, 3)")
        rows = self.cursor.fetchall()  # Получаем все строки

            # 3. Получение имен столбцов для создания словарей
        column_names = [description[0] for description in self.cursor.description]

            # 4. Преобразование списка кортежей в список словарей
        data = []
        for row in rows:
            data.append(dict(zip(column_names, row)))

            # 5. Запись данных в YAML файл
        with open("out/output.yaml", 'w', encoding='utf-8') as yaml_file:
            yaml.dump(data, yaml_file, allow_unicode=True, sort_keys=False, default_flow_style=False)
        return None