#writen by thippo
#python version 3.4.3

class Roulette_Algorithm():
    
    import numpy as np
    
    def __init__(self,value_list):
        assert isinstance(value_list,list),'value_list must be list'
        self.value_array=self.np.array(value_list)
        self.probability_array=(self.value_array/self.value_array.sum()).cumsum()
    
    def __call__(self):
        (t, i) = (self.np.random.random(), 0)
        for p in self.probability_array:
            if p >= t:
                break
            i = i + 1
        return self.value_array[i]

if __name__=='__main__':
    a=Roulette_Algorithm([3])
    print(a())