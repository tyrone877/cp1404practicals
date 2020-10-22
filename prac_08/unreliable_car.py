from prac_08.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        from random import randint
        distance_driven = super().drive(randint(0, 100))
        return distance_driven if distance_driven < self.reliability else distance_driven == 0
