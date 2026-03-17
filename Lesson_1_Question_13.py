import math
a, b, c = float(input("a: ")), float(input("b: ")), float(input("c: "))
d = (b**2) - (4*a*c)

if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Real and Different roots:", r1, r2)
elif d == 0:
    print("Real and Same root:", -b / (2*a))
else:
    print("Complex/Imaginary roots")