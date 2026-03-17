# Logic: (Divisible by 400) OR (Divisible by 4 AND NOT divisible by 100)
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")