from abc import ABC


class GeometricalFigure(ABC):

    def __init__(self, area: int, perimeter: int):
        self.area = area
        self.perimeter = perimeter
        self._name = None
        self._angles = None

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        if not(isinstance(value, int) and value > 0):
            raise ValueError("Not valid value for area attr")
        self._area = value

    @area.deleter
    def area(self):
        raise AttributeError("Area deletion is not allowed")

    @property
    def perimeter(self):
        return self._perimeter

    @perimeter.setter
    def perimeter(self, value):
        if not(isinstance(value, int) and value > 0):
            raise ValueError("Not valid value for perimeter attr")
        self._perimeter = value

    @perimeter.deleter
    def perimeter(self):
        raise AttributeError("Perimeter deletion is not allowed")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name change is not allowed")

    @name.deleter
    def name(self):
        raise AttributeError("Name deletion is not allowed")

    @property
    def angles(self):
        return self._angles

    @angles.setter
    def angles(self, value):
        raise AttributeError("Angles change is not allowed")

    @angles.deleter
    def angles(self):
        raise AttributeError("Angles deletion is not allowed")

    def add_area(self, other_figure):
        if not isinstance(other_figure, GeometricalFigure):
            raise TypeError("The transferred object is not a geometric figure!")
        return self.area + other_figure.area


class Triangle(GeometricalFigure):

    def __init__(self, area, perimeter):
        super().__init__(area, perimeter)
        self._name = "triangle"
        self._angles = 3


class Rectangle(GeometricalFigure):

    def __init__(self, area, perimeter):
        super().__init__(area, perimeter)
        self._name = "rectangle"
        self._angles = 4


class Square(GeometricalFigure):

    def __init__(self, area, perimeter):
        super().__init__(area, perimeter)
        self._name = "square"
        self._angles = 4


class Circle(GeometricalFigure):

    def __init__(self, area, perimeter):
        super().__init__(area, perimeter)
        self._name = "circle"
        self._angles = 0
