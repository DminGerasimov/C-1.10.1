import math

class Figures:
    
    def __init__(self, x, y):   #координаты фигуры
        self.x = x
        self.y = y
    
    def get_coordinates(self):  #кортеж с координатами фигуры
        return self.x, self.y


class Rectangle(Figures):
    
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def get_area(self):
        return self.width * self.height

    def get_string(self):
        return str(f"Rectangle({self.x}, {self.y}, {self.width}, {self.height})")


class Square(Figures):

    def __init__(self, x, y, width):
        self.width = width
        self.x = x
        self.y = y

    def get_area(self):
        return self.width ** 2

    def get_string(self):
        return str(f"Square({self.x}, {self.y}, {self.width})")


class Circle(Figures):

    def __init__(self, x, y, radius):
        self.radius = radius
        self.x = x
        self.y = y

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_string(self):
         return str(f"Circle({self.x}, {self.y}, {self.radius})")

