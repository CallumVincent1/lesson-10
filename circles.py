class Circle:
    def __init__(self):
        self.radius = None 

    def set_radius(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def __str__(self):
        return f"the circle has radius {self.get_radius()} and area = {self.area()}"
        
circle = Circle()
circle.set_radius(5)
print(circle)