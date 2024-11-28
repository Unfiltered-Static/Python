#Given employee tuples
employees = [
    ("John Doe", 101, "Human Resources", 60000),
    ("Alice Smith", 102, "Marketing", 55000),
    ("Bob Johnson", 103, "Engineering", 75000)
]#Iterate and print employee details
for name, id_number, department, salary in employees:
    print(f"Name: {name}, ID: {id_number}, Department: {department}, Salary: ${salary}")
