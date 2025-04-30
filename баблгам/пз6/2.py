class Shape:
    pass


class Polygon(Shape):
    pass


class Quadrilateral(Polygon):
    pass


class Triangle(Polygon):
    pass


class Parallelogram(Quadrilateral):
    pass


class Rectangle(Parallelogram):
    pass


class Square(Rectangle):
    pass


class IsoscelesTriangle(Triangle):
    pass


class EquilateralTriangle(Triangle):
    pass


class Circle(Shape):
    pass


print(issubclass(Circle, Shape))
print(issubclass(Polygon, Shape))
print(issubclass(Circle, Shape))
print(issubclass(Polygon, Shape))

print(issubclass(Triangle, Polygon))
print(issubclass(IsoscelesTriangle, Triangle))
print(issubclass(EquilateralTriangle, Triangle))
