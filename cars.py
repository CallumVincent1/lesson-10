class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def get_brand(self):
        return self.brand
    def get_year(self):
        return self.year
    def describe(self):
        print (f"this car is a {self.get_brand()} {self.get_year()}")
    
car = Car("BMW" , 2023)
car.describe()