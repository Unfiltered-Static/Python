#Creating a list of values
user_values = [1, 6, 8, 9, 4, 10, 1, 3, 4, 6]
#Creating a list for unique values
unique = []
#Finding unique values
for i in user_values:
    if i not in unique:
        unique.append(i)
#Iterating through the list of unique items
print("Duplicate values:")
for i in unique:
    if user_values.count(i) > 1:
        print(i)
