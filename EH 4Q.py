class Shape:
    def area(self):
        return 

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = 3.14159  
        return pi * (self.radius ** 2)  

rectangle = Rectangle(4, 5)
circle = Circle(3)

print("Area of Rectangle:", rectangle.area())  
print("Area of Circle:", circle.area())        
