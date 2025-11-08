class Operator:
    def __init__(self, id, courier_id, order_id, cleint_id):
        self.id = id #PK
        self.courier_id = courier_id #FK
        self.order_id = order_id #FK
        self.cleint_id = cleint_id #FK

class Cleint:
    def __init__(self, id, details, address, order_id, courier_id):
        self.id = id #PK
        self.details = details
        self.address = address
        self.order_id = order_id
        self.courier_id = courier_id

class Courier:
    def __init__(self, id, details, order_id, cleint_id, operator_id, status):
        self.id = id #PK
        self.details = details
        self.order_id = order_id #FK
        self.cleint_id = cleint_id #FK
        self.operator_id = operator_id #FK
        self.status = status

class Order:
    def __init__(self, id, name, status, price):
        self.id = id #PK
        self.name = name
        self.status = status
        self.price = price