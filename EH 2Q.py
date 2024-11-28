def get_numbers():
    try:
        #Getting user input for two numbers
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        
        num1 = float(num1)
        num2 = float(num2)
        
        print("You have successfully entered two numbers!")
    
    except ValueError:
        print("Error: One or both of your inputs are not numerical. Please try again.")

#Calling the function to execute the program
get_numbers()
