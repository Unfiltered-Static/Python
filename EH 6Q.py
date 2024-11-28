class Printer:
    def print_data(self, data, location=None):
        if location is None:
            print(f"Printing data: {data}") 
        else:
            print(f"Printing data: {data} at {location}")  

#Example usage
printer = Printer()

#Calling print_data with one argument
printer.print_data("Hello, World!")

#Calling print_data with two arguments
printer.print_data("Hello, World!", "Office")
