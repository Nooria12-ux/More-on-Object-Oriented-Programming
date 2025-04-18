import math

class Circle:
    
    def __init__(self, r):
        self.r = r
        
    def perimeter(self):
        return 2 * math.pi * self.r
    
    def area(self):
        return math.pi * self.r * self.r
    
radius  = float(input("Enter the Radius: "))

c1 = Circle(radius)

print(f"Perimeter of c1: {c1.perimeter()}")        
print(f"Area of c1: {c1.area()}")