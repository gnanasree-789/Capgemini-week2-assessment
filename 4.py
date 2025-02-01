#Class and Object
# 4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`.
#  Write a method to return student details.

class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
    def student_details(self):
        print(f"Name: {self.name} \nRoll Number: {self.roll_number}")
name=input("Enter the Name of the sudent: ")
Roll_number=int(input("Enter the roll number: "))
student=Student(name,Roll_number)
print("The student details are:")
student.student_details()
