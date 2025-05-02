class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, other):
        return Point((self.x + other.x), (self.y + other.y))
    
    def __add__(self, other):
        return Point((self.x + other.x), (self.y + other.y))
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")

p1 = Point(3, 2)
p2 = Point(6, 3)

# p = p1.sum(p2) # Returns a new point which is sum of p1 and p2

p = p1 + p2 # We overloaded the + operator by __add__() method
p.print_point()