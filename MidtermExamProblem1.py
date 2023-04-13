class Circle:
    def __init__(self, radius=None, diameter=None):
        import math
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            return ValueError("Please enter the value of radius and diameter")
        self.pi = math.pi

    def Area(self):
        return self.pi * self.radius ** 2

    def Perimeter(self):
        return 2 * self.pi * self.radius

    def display(self):
        print("Using the radius the area of the circle is: ", self.Area())
        print("Using the radius the perimeter of the circle is: ", self.Perimeter())


radius1 = float(input("Enter the value of radius in the circle: "))
circle1 = Circle(radius=radius1)
circle1.display()

