# Interface (Using Abstract Base Classes - ABC)
# •	19. Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. 
# Implement it in `Car`, `Bike`, and `Truck` classes.

from abc import ABC,abstractmethod
class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(IVehicle):
    def start_engine(self):
        print("The car is started")
    def stop_engine(self):
        print("The car is stopped")
class Bike(IVehicle):
    def start_engine(self):
        print("The bike is started")
    def stop_engine(self):
        print("The bike is stopped")
class Truck(IVehicle):
    def start_engine(self):
        print("The truck is started")
    def stop_engine(self):
        print("The truck is stopped")

c=Car()
c.start_engine()
c.stop_engine()
b=Bike()
b.start_engine()
b.stop_engine()
t=Truck()
t.stop_engine()
t.stop_engine()