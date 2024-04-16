import csv


class Item:
    pay_rate = 0.8  # class level attribute
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments
        assert price >= 0, f"Price should be equal or greater than 0"
        assert quantity >= 0, f"Quantity should be equal or greater than 0"

        # assign to self object and these are instance level attribute
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=float(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name},'{self.price}', '{self.quantity}')"


class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken phones should be equal or greater than 0"
        self.broken_phones = broken_phones


# item1 = Item("Keyboard", 100, 2)
# item2 = Item("Laptop", 100, 2)
# item3 = Item("Mouse", 10, 1)
# item4 = Item("Phone", 2000, 2)
# item2.pay_rate = 0.7
# print(item2.apply_discount())

# Item.instantiate_from_csv()
# print(Item.all)

# for instance in Item.all:
#     print(instance.name)

# print(Item.is_integer(3.3))
phone1 = Phone("iPhone", 1200, 1, 1)
print(phone1.calculate_total_price())
