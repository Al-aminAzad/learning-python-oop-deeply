import csv


class Item:
    pay_rate = 0.8  # class level attribute
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments
        assert price >= 0, f"Price should be equal or greater than 0"
        assert quantity >= 0, f"Quantity should be equal or greater than 0"

        # assign to self object and these are instance level attribute
        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, incremented_value):
        self.__price = self.__price + self.__price * incremented_value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 5:
            raise Exception("Name is too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

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
        return f"{self.__class__.__name__}('{self.name},'{self.__price}', '{self.quantity}')"

    def __connect(self, smtp):
        pass

    def __email_body(self):
        return f""""
            Hello Jhon,
            Name {self.name}
            """

    def __send(self):
        pass

    def send_email(self):
        self.__connect("")
        self.__email_body()
        self.__send()
