import math

class shape:
    def area(self):
        print("Area not defined")

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius
    
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
shapes = [circle(), rectangle(4, 6)]
for shape in shapes:
    print("Area:", shape.area())