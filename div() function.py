def div(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b  
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = div(num1, num2)
print("The result of dividing", num1, "by", num2, "is:", result)
