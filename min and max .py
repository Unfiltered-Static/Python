numbers = []
for i in range(5):
    num = float(input(f"Enter number {i + 1}: "))  
    numbers.append(num) 
print("The numbers are:", numbers)
maximum = numbers[0]
minimum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num  
    if num < minimum:
        minimum = num  
print("Maximum:", maximum)
print("Minimum:", minimum)
