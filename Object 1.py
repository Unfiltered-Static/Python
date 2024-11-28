class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id  
        self.name = name              
        self.marks = marks            

#Creating a Student object
student1 = Student(87, "Anuv", [85, 90, 78])

#Printing student details
print("Student ID:", student1.student_id)
print("Name:", student1.name)
print("Marks:", student1.marks)
