class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area=Circle.pi * radius * radius
    def get_circumfrence(self):
         return 2 * Circle.pi *self. radius
circle_1=Circle(3)
print(f"The area of Circumferance :",circle_1.get_circumfrence())
print(f"The area of Circle :",circle_1.area)
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def get_area(self):
        return self.length*self.width
rectangle_1=Rectangle(5,4)
print(f"The area of Rectangle :",rectangle_1.get_area())
class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def get_area(self):
        return 0.5 * self.base * self.height
triangle_1=Triangle(6,4)
print(f"The area of Triangle :",triangle_1.get_area())
