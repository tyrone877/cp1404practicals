from prac_06.guitar import Guitar

CURRENT_YEAR = 2020


def test():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 500.00)

    print("{} get_age() - Expected {}.  Got {}".format(guitar.name, 98, guitar.get_age()))

    print("{} get_age() - Expected {}.  Got {}".format(other.name, 7, other.get_age()))

    print("{} is_vintage() - Expected {}.  Got {}".format(guitar.name, True, guitar.is_vintage()))

    print("{} is_vintage() - Expected {}.  Got {}".format(other.name, False, other.is_vintage()))


test()
