class Animal:
    name = "lion"  #class attribute
    
    def __int__(self,age):
        self.age = age #instance attibute
        
    def show(self): #instance method , targets you object's location
        print("how are you? ")
        
    @classmethod
    def hello(cls): #targets your class's location
        print("how are you brother")
        
    @staticmethod
    def static():
        print("how are you")
        

obj = Animal(12)
obj.static()