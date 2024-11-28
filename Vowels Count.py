string = "Welcome to python Training"
lower_string = string.lower()
count = 0
vowels = ["a","e","i","o","u"]
for i in lower_string:
    if i in vowels:
        count +=1     
print(f"The vowels count is {count}")
