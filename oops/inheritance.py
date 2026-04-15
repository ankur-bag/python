#INHERITANCE

# class FactoryMumbai: #parent class / super class
#     a = "I am an attribute mentioned inside Factory"
#     def hello(self):
#         print("hello I am a method mentioned inside Factory")
    

# class FactoryPune(FactoryMumbai): #child class / sub class
#     pass

# obj1 = FactoryMumbai()

# obj2 = FactoryPune()

# print(obj2.hello())



# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def show(self):
#         print(f"hello your name is {self.name}, and age {self.age}")


# class Human(Animal):
#     def __init__(self, name ,age):
#         super().__init__(name)
#         self.age = age

# animal1 = Animal("lion")
# person1 = Human("Ankur",21)
# person1.show()




# Multiple Inheritance

class Animal:
    name1 = "lion"
    def __init__(self,name):
        pass
    
class Human:
    name2 = "ankur"
    def __init__(self,name, age):
        pass

class Robots(Animal,Human):
    name3 = "charli"
   

obj = Robots()

print(obj.name1)
print(obj.name2)
print(obj.name3)


#Multilevel Inheritance
#Grand parent class - Parent class - child class

class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zip
    
class BhopalFactory(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips) #called form parent class
        self.color = color #add ons
        
class PuneFactory(BhopalFactory):
    def __init__(self,material,zips,color,pockets):
        super().__init__(material,zips,color) #called from parent class
        self.pockets = pockets #add ons
        

obj = PuneFactory()