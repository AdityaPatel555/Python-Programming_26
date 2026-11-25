# Assignment 2: Find the largest of three numbers using if-elif-else statements

a = int(input("Enter your 1st number (a): "))
b = int(input("Enter your 2nd number (b): "))
c = int(input("Enter your 3rd number (c): "))

if a > b and a > c:
    print(f"a ({a}) is largest")
elif b > a and b > c:
    print(f"b ({b}) is largest")
elif c > a and c > b:
    print(f"c ({c}) is largest")
elif a == b and b > c:
    print(f"a and b ({a}) are largest")
elif a == c and c > b:
    print(f"a and c ({a}) are largest")
elif b == c and b > a:
    print(f"b and c ({b}) are largest")
else:
    print(f"a, b, and c ({a}) are equal and largest")
