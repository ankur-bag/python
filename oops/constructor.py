# A constructor is a maethod that runs , automatically when we call a class and this constructor function will target th objects location


class Factory:
    def __init__(self,material,zips,pockets): #insiitalization func
        #material , zips and pockets are used as parameters
        # self is used as location transfer
        self.material = material
        self.zips = zips
        self.pockets = pockets
    
    def show(self):
        print(f"your materials are {self.material}, {self.pockets}, {self.zips}")

Factory("leather", 3, 2 )

reebok = Factory("leather", 3,2)
campus =Factory("nylon", 3,3)

reebok.show()