#Given list of tuples
tuples_list = [(1, 2), (3, 4), (5, 6)]
#Initialize a variable to hold the total sum
total_sum = 0
#Loop through each tuple in the list
for tup in tuples_list:
    #Looping through each number in the tuple
    for num in tup:
        #Adding the number to the total sum
        total_sum += num
#Printing the total sum
print("The sum of the numbers in the tuples is:", total_sum)
