import math

class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        print("Area of the circle:",round(math.pi*self.r**2,4))
    def circum(self):
        print("Circumference of the circle: ", round(2*math.pi*self.r,4))

r=float(input("Enter the radius of the circle:"))
c=circle(r)
c.area()
c.circum()

