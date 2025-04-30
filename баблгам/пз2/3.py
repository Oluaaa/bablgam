class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self.color

    def __repr__(self):
        return f"ColoredPoint({self._x}, {self._y}, '{self._color}')"

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self._fields == other._fields
        return NotImplemented

    def __hash__(self):
        return hash(self._fields)

    @property
    def _fields(self):
        return self._x, self._y, self._color


points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}

print(points)
