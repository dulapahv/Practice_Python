class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirCon(self):
        print("Turn On : Air")


class Car(Vehicle):
    pass


class PickUp(Vehicle):
    pass


class Van(Vehicle):
    pass


class EstateCar(Vehicle):
    pass


car1 = Car()
car1.turnOnAirCon()

PickUp1 = PickUp()
PickUp1.turnOnAirCon()

Van1 = Van()
Van1.turnOnAirCon()

EstateCar1 = EstateCar()
EstateCar1.turnOnAirCon()
