def divide_numbers():
    try:
        #Getting user input for two numbers
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        result = numerator / denominator
        print(f"The result of {numerator} divided by {denominator} is {result}.")
    
    except ZeroDivisionError:
         print("Error: You cannot divide by zero. Please try again.")

#Calling the function to execute the program
divide_numbers()
