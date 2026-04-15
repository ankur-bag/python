# ABSTRACTION


from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class square(abstract):
    def __init__(self,side):
        self.side = side
    

class circle(abstract):
    def __init__(self,radius):
        self.radius = radius
    def perimeter(self):
        print("i have created perimeter")
    def area(self):
        print("i have created perimeter")
        
obj = circle(5) #can be executed , coz circle class have perimeter and area func
obj = square(5) #can not be executed , coz square class have no perimeter and area func
