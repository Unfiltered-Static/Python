#Given String
s = "String and String Function"
#Splitting the String
splitting_s = s.split()
#Declaring a result variable
result = ""
#Iterating the splitting_s
for i in splitting_s:
    if i not in result.split():  
        result += i + " "
#Printing the Result
print(result.strip())  
