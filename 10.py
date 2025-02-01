#Inheritance (Multiple, Multi-Level)
# 10. Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`.
#  Demonstrate method overriding and attribute reuse.

class Electronics:
    def __init__(self,price):
        self.price=price
    def show(self):
        print(f"The electronic device price is : {self.price}")
class MobileDevice(Electronics):
    def __init__(self, price, storage):
        super().__init__(price)
        self.storage=storage
    def show(self):
        print(f"The price of Mobile is {self.price} and it has storage of {self.storage}")
class SmartPhone(MobileDevice):
    def __init__(self, price, storage, brand):
        super().__init__(price, storage)
        self.brand=brand
    def show(self):
        print(f"The price of smart phone is {self.price}, Storage is {self.storage}, Brand is {self.brand}")

price=int(input("Enter price: "))
storage=input("Enter storage: ")
brand=input("ENter brand: ")
s=SmartPhone(price,storage,brand)
s.show()