from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():

    total_trip_cost = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            print(f"0 - {taxis[0]} \n1 - {taxis[1]} \n2 - {taxis[2]}")
            taxi_choice = int(input())
            selected_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            travel_distance = int(input("Drive how far? "))
            selected_taxi.start_fare()
            selected_taxi.drive(travel_distance)
            fare_cost = selected_taxi.get_fare()
            print(f"Your {selected_taxi.name} trip cost you ${fare_cost:.2f}")
            total_trip_cost += fare_cost
        else:
            print("Invalid entry!!")
        print(f"Bill to date: ${total_trip_cost:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_trip_cost:.2f}")


main()
