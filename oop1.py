class aec:
    i=12345
    def it(self,a,b):
        print(a+b)
    #return 'welcome to it'
a=aec()
b=aec()
print(a.i)
a.i=2345
print(b.i)
a.it(3,7)
class aec:
    def __init__(self):
        self.a=0
        self.b=0
    def ece(self):
        self.a=int(input())
        self.b=int(input())
        print(self.a+self.b)
a=aec()
a.ece()
