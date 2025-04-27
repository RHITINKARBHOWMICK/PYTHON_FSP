class dept:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
    def printdept(self):
        print("student name: ", self.name , "studies in ", self.dept)
class stud(dept):
            pass
x=stud("mike","CSE")
x.printdept()
        
