def find_largest(num1, num2):
    if num1 > num2:
        print("The largest number is:", num1)
    elif num2 > num1:
        print("The largest number is:", num2)
    else:
        print("Both numbers are equal.")

find_largest(float(input("Enter the first number: ")),
             float(input("Enter the second number: ")))
