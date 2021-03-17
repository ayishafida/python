def rect(l, b):
    x = lambda l, b : l * b
    return x(4, 5)


def sqr(s):
    y = lambda s : s ** 2
    return y(6)


def tri(h, b):
    z = lambda h, b : (h * b) / 2
    return z(8, 4)


r = rect(4, 5)
s = sqr(6)
t = tri(8, 4)
print("Area of rectangle is", r)
print("Area of square", s)
print("Area of triangle", t)

