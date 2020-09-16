from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        name = input("Name: ")

    if guitars:
        guitars.sort()
        print("Print these are my guitars")
        for i, guitar in enumerate(guitars):
            vintage_identifier = ""
            if guitar.is_vintage():
                vintage_identifier = "(vintage)"
            print("Guitar {0}: {1.name:<10} ({1.year}), worth ${1.cost:5,.2f} {2}"
                  .format(i + 1, guitar, vintage_identifier))
        else:
            print("You do not own any guitars!")


main()
