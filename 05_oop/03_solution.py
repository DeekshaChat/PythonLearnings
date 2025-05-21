class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_electric_Car = ElectricCar("Tesla", "Model S", "800 kWh")
print(my_electric_Car.brand)
print(my_electric_Car.fullname())
    