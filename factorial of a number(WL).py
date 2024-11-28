number = int(input("Enter a positive integer to find its factorial: "))
factorial = 1
counter = 1
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    while counter <= number:
        factorial *= counter  
        counter += 1  
    print("The factorial of", number, "is", factorial)
