def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)

num = int(input("Number: "))
print("Factorial:", fact(num))