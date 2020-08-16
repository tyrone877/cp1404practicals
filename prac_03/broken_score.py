"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = return_score_result(score)
    print(result)
    random_score = return_random_score()
    random_score_result = return_score_result(random_score)
    print(f'Random result is {random_score_result}')


def return_score_result(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif 50 <= score < 90:
        return "Passable"
    elif score >= 90:
        return "Excellent"
    else:
        return "Bad"


def return_random_score():
    score = random.randint(0, 100)
    return score


main()
