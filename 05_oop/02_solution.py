class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"{self.brand} {self.model}"
    
my_car = Car("Toyota", "Fortuner")
print(my_car.brand)
print(my_car.fullName())