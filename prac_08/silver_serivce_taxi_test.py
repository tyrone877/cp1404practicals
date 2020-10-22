from prac_08.silver_service_taxi import SilverServiceTaxi

silver_taxi_1 = SilverServiceTaxi("Hummer", 200, 4)
silver_taxi_1.drive(18)
print(silver_taxi_1)
silver_taxi_2 = SilverServiceTaxi("Test ride", 100, 2)
silver_taxi_2.drive(18)
test_ride_fare = silver_taxi_2.get_fare()
print(f"Test ride fare costs ${test_ride_fare}")