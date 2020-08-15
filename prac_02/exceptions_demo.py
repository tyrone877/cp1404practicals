"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

'''
1. When will a ValueError occur?
When a Character is entered in as either the numerator or denominator.

2. When will a ZeroDivisionError occur?
The the value 0 is entered in as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Changes to code applied.
'''