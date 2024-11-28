# Given string
sample = "madamracecar"

#Calculating the length and midpoint
length = len(sample)
midpoint = length // 2

#Slicing the string into two halves
first_half = sample[:midpoint + (length % 2)]  # Include middle character if odd
second_half = sample[midpoint + (length % 2):]

#Checking if the first half reversed equals the second half
if first_half[::-1] == second_half:
    print("The first half is a palindrome of the second half.")
else:
    print("The first half is NOT a palindrome of the second half.")
