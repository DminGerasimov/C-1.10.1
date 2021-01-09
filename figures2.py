from figures import Rectangle, Square, Circle

#прямоугольники
rect1 = Rectangle(2, 3, 4, 5)
rect2 = Rectangle(3, 4, 5, 6)

#штаны спанчбоба
square1 = Square(1, 2, 5)
square2 = Square(3, 4, 6)

#окружности
circle1 = Circle(10, 11, 6)
circle2 = Circle(12, 13, 7)


figures_ = [rect1, square1, circle1, rect2, circle2, square2 ]

for figure in figures_:
    if isinstance(figure,Rectangle):
        #print(f"Figure Rectangle with area {figure.get_area()} & coordinates {figure.get_coordinates()}")
        print(figure.get_string())
    elif isinstance(figure,Square):
        #print(f"Figure Rectangle with area {figure.get_area()} & coordinates {figure.get_coordinates()}")
        print(figure.get_string())
    elif isinstance(figure,Circle):
        #print(f"Figure Rectangle with area {figure.get_area()} & coordinates {figure.get_coordinates()}")
        print(figure.get_string())
    else:
        print("Error in head)")
