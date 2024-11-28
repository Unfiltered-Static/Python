total_sum = 0
end_number = 10  
while True:
    number = int(input("Enter a number (0 to stop or {} to end): ".format(end_number)))
    if number == 0 or number == end_number:
        break  
    total_sum += number
print("The sum of all entered numbers is:", total_sum)
