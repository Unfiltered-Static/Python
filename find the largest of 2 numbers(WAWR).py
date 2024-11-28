def get_largest(a, b):
    if a > b:
        return a
    else:
        return b
first_number = float(input("Please enter the first number: "))
second_number = float(input("Please enter the second number: "))
largest = get_largest(first_number, second_number)
print("The largest number is:", largest)
