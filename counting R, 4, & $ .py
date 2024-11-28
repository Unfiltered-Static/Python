#Given String
s = "P@#yn26at^&i5ve"
#Initializing variables to count
digits = 0
chars = 0
symbols = 0
#Iterating the string and checking using built-in methods
for i in s:
    if i.isalpha():
        chars += 1
    elif i.isdigit():
        digits += 1
    elif not i.isspace():
        symbols += 1
#Printing count of variables
print(f"Chars : {chars}")
print(f"Digits : {digits}")
print(f"Symbols : {symbols}")
