class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def display(self):
        print(f"this animal is a {self.name} and makes the sound {self.sound}")
animal = Animal("cat", "meow")
animal.display()