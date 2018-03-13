"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the number is not a real number, and is not a number eg. square
2. When will a ZeroDivisionError occur?
When the denominator is 0. Division by 0 is not possible
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Tell him he is an idiot. No matter what you do you can't do division by 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    print("Infinity")

print("Finished.")