class MyGreetings:
    def __init__(self,your_name,preferred_food):
        self.name = your_name
        self.food = preferred_food
    
    def greet(self):
        print(f"hello, {self.name}. Welcome to the object oriented programming session")
        print(f"we heard you love {self.food}. Enjoy your session")

first_instance = MyGreetings("alex", "pizza")
second_instance = MyGreetings("joanna" , "cheese burger")
another_instance = MyGreetings("emy", "noodles")
first_instance.greet()
second_instance.greet()
another_instance.greet()