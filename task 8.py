class CarDetails:
    def __init__(self,name,mileage):
        self.car_name = name
        self.miles = mileage

    def drive(self,distance):
        self.miles += distance

    def display(self):
        print(f"the car name is {self.car_name} and has driven {self.miles} miles")


x = CarDetails("john", 1000)

x.display()
        