#Class and Object
#5. Create a `Product` class with attributes `name`, `price`, and `stock`.
#  Write a method `check_availability(quantity)` that returns whether the requested quantity is available.

class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.stock=stock
        self.price=price
    def check_availability(self,qunatity):
        self.quantity=qunatity
        if self.stock >= self.quantity:
            print("requested quantity is available")
        else:
            print("The requested quantity is not avilable")

name=input("Enter name of the product: ")
price=int(input("enter the price: ")) 
stock=int(input("ENter the Stock present: "))         
product=Product(name,price,stock)

quantity=int(input("ENter the quantity you want: "))
product.check_availability(quantity)