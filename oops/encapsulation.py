#ENCAPSULATION

class Demo:
    def __init__(self):
        
        #Access modifiers : 
        self.name = "public member" #public
        self._age = 21 #protected (access in subclass) [just a convection, no as such use]
        self.__salary = 50000  #private (can not access in subclass)
        
    def show(self):
        print("inside the class")
        print("public: ", self.name)
        print("protected: ", self._age)
        print("private: ", self.__salary)
    
obj = Demo()
obj.show()