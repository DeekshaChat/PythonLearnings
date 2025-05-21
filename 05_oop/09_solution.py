class Car:
    def __init__(self, __brand, __model):
        self.__brand = __brand
        self.__model =__model
    
class ElectricCar(Car):
    def __init__(self, __brand, __model, battery_size):
        super().__init__(__brand, __model)
        self.battery_size = battery_size
    

my_electric_car = ElectricCar("Tesla", "Model S", "800kWh")
print(isinstance(my_electric_car, Car))
print(isinstance(my_electric_car, ElectricCar))