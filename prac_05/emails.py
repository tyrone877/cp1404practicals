def main():

    email_to_name = {}

    email = input('Email: ')

    while email != '':
        full_name = return_name_from_email(email)
        confirm_full_name = input(f'Is your name {full_name}? (Y/n) ')
        if confirm_full_name == 'n':
            full_name = input("Name: ").title()
        email_to_name[email] = full_name
        email = input('Email: ')

    for email, full_name in email_to_name.items():
        print(f"{full_name} ({email.lower()})")


def return_name_from_email(email):
    words = email.strip().split('@')
    full_name = words[0].split('.')
    full_name = ' '.join(full_name).title()
    return full_name


main()
