#writen by thippo
#python version 3.4.3

class Rejection_Sampling():

    import random
    import numpy as np
    import matplotlib.pyplot as plt
	
    def __init__(self,target_function,sampling_function,sampling_interval=(-10,10)):
        #assert type(target_function)=='function' ,'wrong'
        #assert type(target_function)=='function' ,'wrong'
        self.target_function=target_function
        self.sampling_function=sampling_function
        self.sampling_interval=sampling_interval
		
    def __call__(self):
        switch=0
        while(switch==0):
            u=self.random.random()
            x=self.random.uniform(self.sampling_interval[0],self.sampling_interval[1])
            if u<self.target_function(x)/self.sampling_function(x):
                switch=1
                return x
    def sampling_array(self,sampling_times=1000,graphic=True):
        u=self.np.array(self.np.random.rand(sampling_times))
        x=self.np.array([self.random.uniform(self.sampling_interval[0],self.sampling_interval[1]) for x in range(sampling_times)])
        x_ratio=self.target_function(x)/self.sampling_function(x)
        if graphic:
            self.plt.hist(x[u<x_ratio],np.arange(self.sampling_interval[0], self.sampling_interval[1], 0.1),normed=True)
            self.plt.plot(range(self.sampling_interval[0],self.sampling_interval[1]),[self.target_function(x) for x in range(self.sampling_interval[0],self.sampling_interval[1])])
            self.plt.show()
        return x[u<x_ratio]

if __name__=='__main__':
    import numpy as np
    def target_function(x):
        return 0.3*np.exp(-0.2*x**2)+0.7*np.exp(-0.2*(x-10)**2)
    def sampling_function(x):
        return 0.8
    a=rejection_sampling(target_function,sampling_function,(-6,20))
    print(a())
    a.sampling_array(sampling_times=10000)