#Inheritance (Multiple, Multi-Level)
# •	6. Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike`
# inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.

class Vehicle:
    def __init__(self,type):
        self.type=type
class Car(Vehicle):
    def __init__(self, type,color):
        super().__init__(type)
        self.color=color
    def Cardetails(self):
        print(f"The type of vehicle is : {self.type}, Color of the car : {self.color}")
class Bike(Vehicle):
    def __init__(self, type,color):
        super().__init__(type)
        self.color=color
    def Bike_details(self):
        print(f"The type of vehicle is : {self.type}, Color of the Bike : {self.color}")
class ElectricCar(Car):
    def __init__(self, type, color,typeOfCar):
        super().__init__(type, color)
        self.typeOfCar=typeOfCar
    def ElectricCar_details(self):
        print(f"The type of vehicle is : {self.type}, Color of the Electric car : {self.color}, Type of the car is : {self.typeOfCar}")

type=input("Enter the type of vehicle: ")
if type.lower() == 'car':
    color=input("ENter the color of the car: ")
    e1=Car(type,color)
    e1.Cardetails()
elif type.lower() == 'bike':
    color=input("ENter the color of the bike: ")
    e2=Bike(type,color)
    e2.Bike_details()
elif type.lower() =='electriccar':
    color=input("ENter the color of the Electric car: ")
    typeofcar=input("ENterthe type of car: ")
    e3=ElectricCar(type,color,typeofcar)
    e3.ElectricCar_details()