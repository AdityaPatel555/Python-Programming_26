# Assignment 5: Check that a string contains only a-z, A-Z, and 0-9
import re

user_text = input("Enter a string: ")

# Regex ^[a-zA-Z0-9]+$ strictly matches ASCII letters (a-z, A-Z) and digits (0-9)
if re.fullmatch(r"[a-zA-Z0-9]+", user_text):
    print("Valid: The string contains only a-z, A-Z, and 0-9.")
else:
    print("Invalid: The string contains characters outside a-z, A-Z, and 0-9 (or is empty).")

# Note: Python's built-in isalnum() also checks alphanumeric characters
print("Using isalnum():", user_text.isalnum())
