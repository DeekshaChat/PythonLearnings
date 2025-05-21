class Car:
    total_car = 0
    def __init__(self, __brand, model):
        self.__brand = __brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return f"{self.__brand}!!"
    
class ElectricCar(Car):
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size
    
Car("Toyota", "Fortuner")
Car("Honda", "Civic")
ElectricCar("Tesla", "Model S", 100)


print(Car.total_car)