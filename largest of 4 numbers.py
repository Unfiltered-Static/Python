def find_largest_of_four(num1, num2, num3, num4):
    if num1 >= num2 and num1 >= num3 and num1 >= num4:
        return num1
    elif num2 >= num3 and num2 >= num4:
        return num2
    elif num3 >= num4:
        return num3
    else:
        return num4
numbers = [float(input(f"Enter number {i+1}: ")) for i in range(4)]
print(f"The largest number is: {find_largest_of_four(*numbers)}")
