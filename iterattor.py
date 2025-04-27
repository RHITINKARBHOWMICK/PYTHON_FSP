class mynum:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=4:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
mycl=mynum()
myitr=iter(mycl)
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))
