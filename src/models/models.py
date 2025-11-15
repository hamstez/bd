class Operator:
    def __init__(self, id, courier_id, order_id, client_id):
        self.id = id #PK
        self.courier_id = courier_id #FK
        self.order_id = order_id #FK
        self.client_id = client_id #FK

class Client:
    def __init__(self, id, details, address, order_id, courier_id):
        self.id = id #PK
        self.details = details
        self.address = address
        self.order_id = order_id
        self.courier_id = courier_id

class Courier:
    def __init__(self, id, details, order_id, client_id, operator_id, status, password):
        self.id = id #PK
        self.details = details
        self.order_id = order_id #FK
        self.client_id = client_id #FK
        self.operator_id = operator_id #FK
        self.status = status
        self.password = password

class Order:
    def __init__(self, id, name, status, price, courier_id):
        self.id = id #PK
        self.name = name
        self.status = status
        self.price = price
        self.courier_id = courier_id