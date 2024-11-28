#Creating a dictionary with names and ages
people = {
    "Vishh": 30,
    "Varun": 25,
    "Subash": 35,
    "Aryan": 40,
    "Eva": 28
}

#Adding a new person to the dictionary
people["SRK"] = 32
print("After adding SRK:", people)

#Updating the age of one person (e.g., update Bob's age)
people["Varun"] = 26
print("After updating Varun's age:", people)

#Removing one person from the dictionary (e.g., remove Charlie)
if "Subash" in people:
    del people["Subash"]
    print("After removing Subash:", people)
else:
    print("Subash not found in the dictionary.")

#Checking if a given key exists in the dictionary
key_to_check = "Vishh"
if key_to_check in people:
    print(f"{key_to_check} exists in the dictionary with age {people[key_to_check]}.")
else:
    print(f"{key_to_check} does not exist in the dictionary.")
