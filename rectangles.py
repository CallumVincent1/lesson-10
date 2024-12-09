class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def find_area(self):
        return self.width * self.length
    def find_perimiter(self):
        return (2*self.width) + (2*self.length)
    
    def display_info(self):
        print(f"the length of the rectangle is {self.length} and the width is {self.width} and the area is {self.find_area()} and the perimiter is {self.find_perimiter()}")
        
rectangle = Rectangle(3,5)
rectangle.display_info()