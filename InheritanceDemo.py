class Base:

    def getA(self,a):
        self.a=a
        return self.a
    def printA(self):
        print("A : ",self.a)

class Derived(Base):

    def getB(self,b):
        self.b=b
        return self.b
    def printB(self):
        print("B : ",self.b)

class Subderived(Base):

    def getC(self,c):
        self.c=c
        return self.c
    def printC(self):
        print("C : ",self.c)

class Subderived1(Derived,Subderived):

    def getD(self,d):
        self.d=d
        return self.d
    def printD(self):
        print("D : ",self.d)
        
sd1=Subderived1()

sd1.getA(10)
sd1.getB(20)
sd1.getC(30)
sd1.getD(40)

sd1.printA()
sd1.printB()
sd1.printC()
sd1.printD()
