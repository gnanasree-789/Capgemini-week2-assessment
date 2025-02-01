# Interface (Using Abstract Base Classes - ABC)
# •	16. Create an interface `IShape` with an abstract method `calculate_area()`.
#  Implement it in `Rectangle` and `Circle` classes.

from abc import ABC,abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(IShape):
    def calculate_area(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print(f"Area of the rectangle: {self.length * self.breadth}")
class Circle(IShape):
    def calculate_area(self,radius):
        self.radius=radius
        print(f"Area of the Circle: {3.14 * self.radius *self.radius}")
r=Rectangle()
length=int(input("Enter the length of the rectangle: "))
breadth=int(input("Enter the breadth of the breadth: "))
r.calculate_area(length,breadth)

c=Circle()
radius=int(input("Enter the radius of the circle: "))
c.calculate_area(radius)