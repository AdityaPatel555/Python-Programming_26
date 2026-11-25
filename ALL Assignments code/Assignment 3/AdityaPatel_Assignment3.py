# Assignment 3: Check whether a triangle is right-angled using a function
import math


def is_right_angled_triangle(a, b, c):
    """Return True if side lengths a, b, c form a valid right-angled triangle."""
    if a <= 0 or b <= 0 or c <= 0:
        return False

    sides = sorted([a, b, c])
    # Check triangle inequality before checking Pythagoras theorem
    if sides[0] + sides[1] <= sides[2]:
        return False

    return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)


side1 = float(input("Enter length of 1st side: "))
side2 = float(input("Enter length of 2nd side: "))
side3 = float(input("Enter length of 3rd side: "))

if is_right_angled_triangle(side1, side2, side3):
    print("The given triangle is a right-angled triangle.")
else:
    print("The given triangle is NOT a right-angled triangle.")
