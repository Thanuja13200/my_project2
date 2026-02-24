class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

l1 = Laptop("Lenovo", 55000)
print(l1.brand, l1.price)