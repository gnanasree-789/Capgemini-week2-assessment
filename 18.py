# Interface (Using Abstract Base Classes - ABC)
# •	18. Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. 
# Create a `BasicCalculator` class that implements these methods.

from abc import ABC,abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass
    @abstractmethod
    def subtract(self,a,b):
        pass
    @abstractmethod
    def multiply(self,a,b):
        pass
    @abstractmethod
    def divide(self,a,b):
        pass
class BasicCalculator(ICalculator):
    def add(self,a,b):
        print(f"Adding {a} and {b} is {a+b}")
    def subtract(self,a,b):
        print(f"subtracting {a} and {b} is {a-b}")
    def multiply(self,a,b):
        print(f"Multiplying {a} and {b} is {a*b}")
    def divide(self,a,b):
        print(f"Dividing {a} and {b} is {a/b}")

a=int(input("ENter the a value: "))
b=int(input("Enter the b value: "))
bc=BasicCalculator()
bc.add(a,b)
bc.subtract(a,b)
bc.multiply(a,b)
bc.divide(a,b)