class Operator:
    def __init__(self, id, cleint_address, order_status, courier_id, cleint_details, courier_details, order_id):
        self.id = id #PK
        self.cleint_address = cleint_address  #FK
        self.order_status = order_status #FK
        self.courier_id = courier_id #FK
        self.cleint_details = cleint_details #FK
        self.courier_details = courier_details #FK
        self.order_id = order_id #FK

class Cleint:
    def __init__(self, id, details, address, order_status, courier_details, order_name, order_id):
        self.id = id #PK
        self.details = details
        self.address = address
        self.order_status = order_status #FK
        self.courier_details = courier_details #FK
        self.order_name = order_name #FK
        self.order_id = order_id

class Courier:
    def __init__(self, id, details, order_id, address_cleint, order_status, cleint_details):
        self.id = id #PK
        self.details = details
        self.order_id = order_id #FK
        self.address_cleint = address_cleint #FK
        self.order_status = order_status #FK
        self.cleint_details = cleint_details #FK

class Order:
    def __init__(self, id, name, status, price):
        self.id = id #PK
        self.name = name
        self.status = status
        self.price = price