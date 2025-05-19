from customer import Customer
from coffee import Coffee
from order import Order

# customer1 = Customer("Eddie")
# customer2 = Customer("Max")

# coffee1 = Coffee("Espresso")
# coffee2 = Coffee("Latte")

# order1= Order(customer1, coffee1, 5.0)  
# print(order1.customer.name)  
# print(order1.coffee.name)    

# order1.customer.name = "John"
# print(order1.customer.name)

# coffee1.orders()
# print(coffee1.orders())

latte = Coffee("Latte")
espresso = Coffee("Espresso")
eddie = Customer("Eddie")

eddie.create_order(latte, 4.0)
eddie.create_order(latte, 4.5)
eddie.create_order(espresso, 3.0)

eddie.coffees()
print(eddie.coffees())

latte.num_orders()
print(latte.num_orders())