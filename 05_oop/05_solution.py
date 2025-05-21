class Car:
    def __init__(self, __brand, model):
        self.__brand = __brand
        self.model = model

    def fuel_type(self):
        return "Petrol/Deisel/CNG"
    
class ElectricCar(Car):
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.batter_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"
    
my_car = Car("Toyota", "Fortuner")
my_electric_car = ElectricCar("Tesla", "Model S", "800kWh")

print(my_car.fuel_type())
print(my_electric_car.fuel_type())