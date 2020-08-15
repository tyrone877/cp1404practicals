"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

BONUS_LESS_THAN_1000 = 0.1
BONUS_GREATER_THAN_1000 = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        user_bonus = sales * BONUS_LESS_THAN_1000
        print(f"Bonus is ${user_bonus:.2f}")
    else:
        user_bonus = sales * BONUS_GREATER_THAN_1000
        print(f"Bonus is ${user_bonus:.2f}")
    sales = float(input("Enter sales: $"))