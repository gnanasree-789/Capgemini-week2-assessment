#Inheritance (Multiple, Multi-Level)
#8. Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.	

class Animal:
    def speak(self):
        print("Animal is speaking")
class Dog(Animal):
    def speak(self):
        print("Dog is barking")
class Cat(Animal):
    def speak(self):
        print("Cat is hissing")
c=Cat()
c.speak()
d=Dog()
d.speak()