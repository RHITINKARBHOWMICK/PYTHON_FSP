class dept:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
    def printdept(self):
        print("student name: ", self.name , "studies in ", self.dept)
class loc(dept):
    def reci(self,loca):
       print("student stays at ",loca)
class stud(loc):
    pass
x=stud("mike","CSE")
x.printdept()
x.reci("kolkata")
