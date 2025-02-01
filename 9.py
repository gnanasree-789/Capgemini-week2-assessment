#Inheritance (Multiple, Multi-Level)
#9. Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `defAirplane`. 
# Handle potential conflicts in the `move()` method

class Car:
    def move(self):
        print("It is car")
class DefAirplane:
    def move(self):
        print("It is Airplane")
class FlyingCar(Car,DefAirplane):
    def __init__(self):
        super().__init__()
    def move(self):
        print("It is inheriting from both classes")
f=FlyingCar()
f.move()