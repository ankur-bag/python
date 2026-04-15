# Object oriented Programming 

 # class --> Attibutes and Methods 
 
class Factory:
    a= 12 #attribute
    
    def hello(self): #methods
        print("how are you")
    
    print("hello how are you? I am getting initialized")

Factory().hello()
obj = Factory() #object -> have all the pwoers of class Factory
print(obj.a)