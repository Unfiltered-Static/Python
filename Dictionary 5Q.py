#Student nested dictionary
student = {
    "name": "Alice",
    "subjects": {"Math": 95, "Science": 88, "English": 92},
    "age": 20
}

#Accessing and printing Science score
print("Alice's Science score:", student["subjects"]["Science"])

#Updating Math score to 98
student["subjects"]["Math"] = 98
print("Updated Math score:", student["subjects"]["Math"])

#Employees nested dictionary
employees = {
    "emp1": {"name": "SRK", "department": "HR"},
    "emp2": {"name": "KRK", "department": "Finance"},
    "emp3": {"name": "ANUV", "department": "IT"}
}

#Displaying each employee's name and department
print("\nEmployee Details:")
for emp in employees.values():
    print(f"Employee Name: {emp['name']}, Department: {emp['department']}")
