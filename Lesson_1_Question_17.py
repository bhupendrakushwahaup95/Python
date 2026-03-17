terms = int(input("Terms: "))
a, b, count = 0, 1, 0
while count < terms:
    print(a, end=" ")
    a, b = b, a + b
    count += 1