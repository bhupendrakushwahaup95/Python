n = int(input("Enter a number: "))
fact = 1
if n < 0:
    print("Not defined for negatives.")
elif n == 0:
    print("Factorial is 1")
else:
    for i in range(1, n + 1):
        fact *= i
    print("Factorial is:", fact)