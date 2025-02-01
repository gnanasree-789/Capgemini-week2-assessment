#Class and Object
# •	1. Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and 
# assign values dynamically.

class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    def show(self):
        print(f"The employee name: {self.name} \nEmployee Id: {self.id} \nEmployee department: {self.department}")

name=input("Enter the employee name: ")
id=int(input("Enter the employee id: "))
department=input("Enter the employee department: ")
employee=Employee(name,id,department)
employee.show()
