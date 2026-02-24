class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

class Square:
    def __init__(self, s):
        self.s = s
    def area(self):
        return self.s * self.s

shapes = [Circle(3), Square(4)]

for shape in shapes:
    print("Area:", shape.area())