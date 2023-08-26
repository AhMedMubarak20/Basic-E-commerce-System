class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

product1 = Product("Laptop", 999.99)
product2 = Product("Phone", 399.99)

cart = ShoppingCart()
cart.add_item(product1)
cart.add_item(product2)

print(f"Total price: ${cart.calculate_total():.2f}")
