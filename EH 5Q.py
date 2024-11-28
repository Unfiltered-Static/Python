class Vector:
    def __init__(self, x, y):
        self.x = x  
        self.y = y  

    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x  
            new_y = self.y + other.y  
            return Vector(new_x, new_y)  
        return NotImplemented  

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

vector1 = Vector(2, 3)
vector2 = Vector(4, 5)

result = vector1 + vector2


print("Result of addition:", result)   
