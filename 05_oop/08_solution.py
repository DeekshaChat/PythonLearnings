class Car:
    def __init__(self, __brand, __model):
        self.__brand = __brand
        self.__model =__model

    def get_brand(self):
        return f"{self.__brand}!!"
    
    @property
    def model_of_car(self):
        return f"{self.__model}"
    
my_car = Car("Toyota", "Fortuner")
print(my_car.model_of_car)