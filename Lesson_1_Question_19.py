s = input("String: ").lower()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")