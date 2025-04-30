class Item:
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return f"{self._name[0].upper()}{self._name[1:]}"

    @property
    def total(self):
        return self.price * self.quantity


fruit = Item('banana', 15, 5)

print(fruit.price)
print(fruit.quantity)
