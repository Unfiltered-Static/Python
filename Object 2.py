class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def display_details(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}, "
              f"Total: {self.total_marks()}, Average: {self.average_marks():.2f}")

#Creating Student objects
student1 = Student(98, "Anuv", [85, 90, 78])
student2 = Student(99, "K.K", [88, 76, 92])
student3 = Student(97, "AP Dhillon", [90, 85, 80])

#Displaying details for each student
student1.display_details()
student2.display_details()
student3.display_details()
