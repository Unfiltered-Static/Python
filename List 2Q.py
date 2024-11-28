#Creating a list of values
user_values = [1, 6, 8, 9, 4, 10]
#Creating small and big variables
small = user_values[0]
big = user_values[0]
#Iterating through the list of items
for i in user_values:
    if i < small:
        small = i
    elif i > big:
        big = i
#Printing small and big values
print("Smallest value:", small)
print("Largest value:", big)
