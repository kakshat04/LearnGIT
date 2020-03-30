from math import pi


class TestCalculate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Object of TestCalculte Class"

    @property
    def addition(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self, y):
        if y==0:
            raise ValueError
        return self.x / y


def modulus(x,y):
    if y == 0:
        raise ValueError
    return x%y


class TestArea:
    def __init__(self, r):
        self.r = r

    def circle(self):
        if self.r <= 0:
            raise ValueError
        return pi * (self.r ** 2)


if __name__ == '__main__':
    obj = TestCalculate(10, 5)
    print(obj.addition)
    print(obj.subtract())
    print(obj.multiply())
    print(obj.divide(2))


