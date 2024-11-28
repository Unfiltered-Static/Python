number = input("Enter a number to check if it is a palindrome: ")
reversed_number = ""
index = len(number) - 1
while index >= 0:
    reversed_number += number[index]  
    index -= 1  
if number == reversed_number:
    print(number, "is a palindrome.")
else:
    print(number, "is not a palindrome.")
