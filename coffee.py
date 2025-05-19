
class Coffee:
    def __init__(self, name,):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 3 :
            raise ValueError("Name must be at least 3 characters long")
        self._name = name
    @property
    def name(self):
        return self._name
    
    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0.0
        total_price = sum(order.price for order in orders)
        return total_price / len(orders)
    def __repr__(self):
        return f"<Coffee name={self.name}>"