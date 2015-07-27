class rejection_sampling():
    import random
    import numpy as np
    import matplotlib.pyplot as plt
    def __init__(self,target_function,sampling_function,sampling_interval=(-10,10),sampling_times=1000):
        #assert type(target_function)=='function' ,'wrong'
        #assert type(target_function)=='function' ,'wrong'
        self.target_function=target_function
        self.sampling_function=sampling_function
        self.sampling_interval=sampling_interval
        self.sampling_times=sampling_times
    def __call__(self):
        switch=0
        while(switch==0):
            u=random.random()
            x=random.uniform(self.sampling_interval[0],self.sampling_interval[1])
            if u<self.target_function(x)/self.sampling_function(x):
                switch=1
                return x
    def get_sampling_array(self,graphic=True):
        u=np.array(np.random.rand(self.sampling_times))
        x=np.array([random.uniform(self.sampling_interval[0],self.sampling_interval[1]) for x in range(self.sampling_times)])
        x_ratio=self.target_function(x)/self.sampling_function(x)
        if graphic:
            plt.hist(x[u<x_ratio],np.arange(self.sampling_interval[0], self.sampling_interval[1], 0.1),normed=True)
            plt.plot(range(self.sampling_interval[0],self.sampling_interval[1]),[self.target_function(x) for x in range(self.sampling_interval[0],self.sampling_interval[1])])
            plt.show()
        return x[u<x_ratio]

if __name__=='__main__':
    import numpy as np
    def target_function(x):
        return 0.3*np.exp(-0.2*x**2)+0.7*np.exp(-0.2*(x-10)**2)
    def sampling_function(x):
        return 0.8
    a=rejection_sampling(target_function,sampling_function,(-6,20),10000)
    a.get_sampling_array(graphic=True)