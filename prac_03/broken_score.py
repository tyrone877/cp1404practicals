"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))

if score > 100 or score < 0:
    print("Invalid score")
elif 50 <= score < 90:
    print("Passable")
elif score >= 90:
    print("Excellent")
else:
    print("Bad")
