MINIMUM_PASSWORD_LENGTH = 5

password = input("Enter in your password: ")
while len(password) < 5:
    print("Your password must be at least 5 characters long, please re-enter your password")
    password = input("Enter in your password: ")
password_length = len(password)
print(password_length * "*")