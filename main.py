from keyboard import Keyboard

item1 = Keyboard("MyItem", 750)
# item1.name = "okoiou"
item1.apply_increment(0.2)
item1.apply_discount()
item1.send_email()
print(item1.price)
