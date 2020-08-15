MINIMUM_PASSWORD_LENGTH = 5


def main():
    password = get_password()
    print_password_length(password)


def print_password_length(password):
    password_length = len(password)
    print(password_length * "*")


def get_password():
    password = input("Enter in your password: ")
    while len(password) < 5:
        print("Your password must be at least 5 characters long, please re-enter your password")
        password = input("Enter in your password: ")
    return password


main()
