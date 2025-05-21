class Battery:
    def battery_info(self):
        return "This is a battery"


class Engine:
    def engine_info(self):
        return "This is an engine"


class ElectricCar(Battery, Engine):
    pass

my_electric_car = ElectricCar()
print(my_electric_car.battery_info())
print(my_electric_car.engine_info())