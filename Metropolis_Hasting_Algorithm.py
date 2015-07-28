#writen by thippo
#python version 3.4.3

class metropolis_hasting_algorithm():
    import math
    import random
    import numpy as np
    import matplotlib.pyplot as plt
	
    def __init__(self,target_function,sampling_interval=(-10,10),gaussian_sd=10):
        self.target_function=target_function
        self.gaussian_sd=gaussian_sd
        self.sampling_interval=sampling_interval
        self.sampling_data_list=[]

    def box_muller_transform(self,mean,sd):
        u1=self.random.random()
        u2=self.random.random()
        Z=self.math.sqrt(-2*self.math.log(u2))*self.math.cos(2*self.math.pi*u1)
        return mean+(Z*sd)
    
    def gaussian(self,x,mean,sd):
        result=(self.math.exp((x-mean)**2/((-2)*sd**2)))/(self.math.sqrt(2*math.pi)*sd)
        return result

    def sampling_list(self,sampling_times=5000,graphic=True):
        x0=0
        print(x0)
        for i in range(sampling_times):
            u=self.random.random()
            x_new=self.box_muller_transform(x0,self.gaussian_sd)
            l=(self.target_function(x_new)*self.gaussian(x0,x_new,self.gaussian_sd))/(self.target_function(x0)*self.gaussian(x_new,x0,self.gaussian_sd))
            if u < min(1,l):
                x0=x_new
                self.sampling_data_list.append(x0)
        if graphic:
            self.plt.hist(self.sampling_data_list,self.np.arange(self.sampling_interval[0], self.sampling_interval[1], 0.1),normed=True)
            self.plt.plot(range(self.sampling_interval[0],self.sampling_interval[1]),[self.target_function(x) for x in range(self.sampling_interval[0],self.sampling_interval[1])])
            self.plt.show()
        return self.sampling_data_list

if __name__=='__main__':
    import math
    import random
    def p(x):
        return float(0.3*math.exp(-0.2*x**2)+0.7*math.exp(-0.2*(x-10)**2))
    a=metropolis_hasting_algorithm(p,sampling_interval=(-50,50))
    a.sampling_list(sampling_times=10000)