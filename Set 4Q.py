#Define the two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

#Get elements present in either set1 or set2 but not in both
unique_elements = set1.symmetric_difference(set2)  #or unique_elements = set1 ^ set2

#Print the result
print("Elements present in Set A or B, but not both:", unique_elements)
