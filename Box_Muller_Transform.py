#writen by thippo
#python version 3.4.3

class Box_Muller_Transform():
    import random
    import math
    def __init__(self,mean=0,sd=1):
        self.mean=mean
        self.sd=sd
    def __call__(self):
        u1=self.random.random()
        u2=self.random.random()
        Z=self.math.sqrt(-2*self.math.log(u2))*self.math.cos(2*self.math.pi*u1)
        return self.mean+(Z*self.sd)

if __name__=='__main__':
    sampling=Box_Muller_Transform(2,3)
    print(sampling())