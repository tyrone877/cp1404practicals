"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = return_converted_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = return_converted_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f}")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def return_converted_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius


def return_converted_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
