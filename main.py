class Item:
    pay_rate = 0.8 #class level attribute
    all =[]
    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments
        assert price >= 0, f'Price should be equal or greater than 0'
        assert quantity >= 0, f'Quantity should be equal or greater than 0'
        
        #assign to self object and these are instance level attribute
        self.name = name
        self.price =price
        self.quantity = quantity

        Item.all.append(self)
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        return self.price * self.pay_rate
    def __repr__(self):
        return f"Item('{self.name},'{self.price}', '{self.quantity}')"

item1 = Item('Keyboard',100,2)
item2 = Item('Laptop',100,2)
item3 = Item('Mouse',10,1)
item4 = Item('Phone',2000,2)
# item2.pay_rate = 0.7
# print(item2.apply_discount())
print(Item.all)

# for instance in Item.all:
#     print(instance.name)