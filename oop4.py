import math
class circle:
    def  r (self,rad):
        self.rad=rad
    def area(self):
        return math.pi * self.rad ** 2
    def peri(self):
        return 2 *math.pi * self.rad
