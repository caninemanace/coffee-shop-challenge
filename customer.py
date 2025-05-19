
class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value
        
    def orders(self):
        from order import Order
        return[order for order in Order.all if order.customer == self]
    
    def coffees(self):
        from order import Order
        unique_coffees = set()
        for order in self.orders():
            unique_coffees.add(order.coffee)
        return list(unique_coffees)
    

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    
    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        customer_totals = {}

        for order in Order.all:
            if order.coffee == coffee:
                customer = order.customer
                customer_totals[customer] = customer_totals.get(customer, 0) + order.price

        if not customer_totals:
            return None

        return max(customer_totals, key=customer_totals.get)
    def __repr__(self):
        return f"<Customer name={self.name}>"

