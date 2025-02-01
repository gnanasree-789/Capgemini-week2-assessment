#Inheritance (Multiple, Multi-Level)
# 7. Create a multi-level class structure with 
# `Person` → `Employee` → `Manager`, where `Manager` has an additional method `approve_leave()`.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self, name,age,id):
        super().__init__(name, age)
        self.id=id
class Manager(Employee):
    def __init__(self, name, age, id, department):
        super().__init__(name, age, id)
        self.department=department
    def approve_leave(self):
        print(f"The Manager is approved leave to the EMployee {self.name} with age {self.age} and the id is {self.id} and department: {self.department}")

name=input("Enter the name of employee: ")
age=int(input("ENter the age of employee: "))
id=int(input("enter the id of the employee: "))
department=input("Enter the department: ")
m=Manager(name,age,id,department)
m.approve_leave()