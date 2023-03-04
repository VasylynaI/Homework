# Exercise 1
# Доопрацюйте класс Pоint з наняття наступним чином: додайте перевірку координат x та y на числа за допомогою property
class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self._x = value
        else:
            raise TypeError("x must be a number")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self._y = value
        else:
            raise TypeError("y must be a number")


# Exercise 2
# Доопрацюйте класс Line з заняття наступним чином: додайте можливість порівнювати лінії по довжині
# (==, !=, >=, <=, >, <) за допомогою відповідних методів

class Line:
    begin = None
    end = None

    def __init__(self, begin_point, end_point):
        self.begin = begin_point
        self.end = end_point

    def _check_data_type(self, other):
        if not isinstance(other, Line):
            raise TypeError("Impossible to compare. Data types are different")

    def length(self):
        return ((self.end.x - self.begin.x) ** 2 + (self.end.y - self.begin.y) ** 2) ** 0.5

    def __eq__(self, other):
        return self.length() == other.length()

    def __ne__(self, other):
        return self.length() != other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __lt__(self, other):
        return self.length() < other.length()


# Example

def compare_lines(line1, line2):
    if line1 == line2:
        print('The lines are equal')

    if line1 != line2:
        print('The lines are not equal')

    if line1 >= line2:
        print('Line 1 is greater than or equal to Line 2')

    if line1 <= line2:
        print('Line 2 is greater than or equal to Line 1')

    if line1 > line2:
        print('Line 1 is more than Line 2')

    if line1 < line2:
        print('Line 2 is more than Line 1')


line1 = Line(Point(0, 0), Point(1, 6))
line2 = Line(Point(0, 0), Point(4, -2))

compare_lines(line1, line2)
