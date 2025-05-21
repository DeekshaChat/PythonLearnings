class Car:
    def __init__(self, __brand, model):
        self.__brand = __brand
        self.model = model
    
    def get_brand(self):
        return f"{self.__brand}!!"
    
    def fullname(self):
        return f"{self.__brand} {self.model}"
    
my_car = Car("Toyota", "Fortuner")
print(my_car.get_brand())