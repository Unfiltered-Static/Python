name = input("Enter your name: ")
lowercase_name = ""
for char in name:
    if 'A' <= char <= 'Z':
        lowercase_char = chr(ord(char) + 32)
    else:
        lowercase_char = char
    lowercase_name += lowercase_char
print("Your name in lowercase is:", lowercase_name)
