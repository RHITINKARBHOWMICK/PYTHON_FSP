class animal:
    def info(self):
           print("animal")
class pet():
    def info(self):
        print("pet")
class dog(animal,pet):
    pass
x=dog()
x.info()
    
                 
