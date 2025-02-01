# Polymorphism
# •	13. Develop a `Shape` class with a method `area()`. 
# Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.

class Shape:
    def area(self):
        print("Area of the given shape: ")
class Square:
    def area(self,side):
        self.side=side
        print(f"Area of the Square is {self.side*self.side}")
class Traingle:
    def area(self,base,height):
        self.base=base
        self.height=height
        print(f"Area of Triangle is : {0.5 * self.base * self.height}")
print("Select any shape: \n1.Square \n2.Triangle")
option=int(input("Enter the option"))
if option == 1:
    side=int(input("Enter the side of the square: "))
    s=Square()
    s.area(side)
elif option == 2:
    base=int(input("Enter the base of the triangle: "))
    height=int(input("Enter the height of the triangle: "))
    t=Traingle()
    t.area(base,height)