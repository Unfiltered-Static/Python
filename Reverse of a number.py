number = input("Enter a number to reverse: ")
reversed_number = ""
index = len(number) - 1
while index >= 0:
    reversed_number += number[index]
    index -= 1  
print("Reversed number:", reversed_number)
