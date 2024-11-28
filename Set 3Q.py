#Define the two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

#Combine both sets to get unique items
unique_items = set1.union(set2)  # or unique_items = set1 | set2

#Print the result
print("Unique items from both sets:", unique_items)
