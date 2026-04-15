# POLYMORPHISM --> same name , diff work (basically it overrides)

# Two ways to achieve polymorphism -> overriding, overlaoding(can't have in python)
 
class Animal:
    def show(self):
        print("hello i am Ankur")

class Human(Animal):
    def show(self):
        print("How are you?")

obj = Human()
obj.show() # the Human's class's function will run , coz it overrided the Animal class's func