import math
import turtle


class CircleObject:

    def __init__(self, radius):
        self.radius = radius

    def input_attribute(self):
        self.radius = float(input("Nceda ufake iradiyasi:"))

    def output(self):
        t = turtle.Turtle()
        t.circle(self.radius)
        print("indawo yesangqa:", calc_area(self))
        print("Iparameter:", calc_perimeter(self))


def calc_area(self):
    a = math.pi * self.radius * self.radius
    return a


def calc_perimeter(self):
    peri = 2 * math.pi * self.radius
    return peri


if __name__ == '__main__':

    obj = CircleObject(0)
    obj.input_attribute()
    obj.output()


