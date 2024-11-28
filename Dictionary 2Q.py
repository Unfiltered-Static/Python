#Defining the dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

#Create a new dictionary and concatenate the others
#Usinging the update() method
new_dict = dic1.copy()  # Creating a copy of the first dictionary
new_dict.update(dic2)   # Updating it with the second dictionary
new_dict.update(dic3)   # Updating it with the third dictionary

#Printing the new concatenated dictionary
print("Concatenated dictionary:", new_dict)
