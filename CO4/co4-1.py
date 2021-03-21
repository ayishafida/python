class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b
        self.l = int(input("enter length:"))
        self.b = int(input("enter breadth:"))

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)


r1 = Rectangle(4, 7)
r2 = Rectangle(3, 4)
a1 = r1.area()
a2 = r2.area()
p1 = r1.perimeter()
p2 = r2.perimeter()

print("area1:", a1)
print("area2:", a2)
print("pm1:", p1)
print("pm2:", p2)
if a1 > a2:
    print("first rectangle has bigger area than second rectangle")
else:
    print("second rectangle has bigger area than first rectangle")
if p1 > p2:
    print("first rectangle has bigger perimeter than second rectangle")
else:
    print("second rectangle has bigger perimeter than first rectangle")