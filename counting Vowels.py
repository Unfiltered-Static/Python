# Given String
s = "Welcome to Python Assignment"
#Declaring variable to count vowels
count = 0
#Creating a set of vowels to check the vowels present in the given string
vowels = ["a", "e", "i", "o", "u"]
#Converting the given string into lowercase
lower_s = s.lower()
#Iterating the lowercase string
for i in lower_s:
    if i in vowels:
        count += 1
#Printing the count
print(f"The vowels count is {count}")
