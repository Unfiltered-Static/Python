#Creating a list of values
user_values = [1, 1, 2, 3, 4, 4, 5, 1]
#First half (up to the middle index)
middle_index = len(user_values) // 2
first_half = user_values[:middle_index]
#Second half (from the middle index onward)
second_half = user_values[middle_index:]
#Printing first and second half
print("First half:", first_half)
print("Second half:", second_half)
