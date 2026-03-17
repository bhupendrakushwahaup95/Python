import math
num = int(input("Number: "))
is_prime = num > 1
for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        is_prime = False
        break
print("Prime" if is_prime else "Not Prime")