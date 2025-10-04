class Circle:
    pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.pi * (self.radius ** 2)
    
    def circumference(self):
        return 2 * Circle.pi * self.radius

r = int(input("Enter radius of circle: "))
c = Circle(r)
print("Area is:", c.area())
print("Circumference is:", c.circumference())