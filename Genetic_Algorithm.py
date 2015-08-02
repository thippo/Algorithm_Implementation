#writen by thippo
#python version 3.4.3
#reference http://garfileo.is-programmer.com/2011/2/19/hello-ga.24563.html
#reference http://blog.csdn.net/emiyasstar__/article/details/6938608

class Genetic_Algorithm():
    
    import random
    import numpy as np
    
    def __init__(self,population_size=50,interval=(-10,10,6),fitness_function='',crossover_probability=0.8,mutation_probability=0.2):
        self.population_size=population_size
        self.interval=interval
        self.chromosome_size=self.encode_length()
        self.fitness_function=fitness_function
        self.crossover_probability=crossover_probability
        self.mutation_probability=mutation_probability
        self.population_list=[self.random.randint(0,2**self.chromosome_size-1) for x in range(self.population_size)]
    
    def encode_length(self):
        i=0
        while (self.interval[1]-self.interval[0])*10**self.interval[2] > 2**i: i+=1
        return i

    def decode(self,chromosome):
        n =  2 ** self.chromosome_size -1
        return (self.interval[0] + chromosome * (self.interval[1]-self.interval[0]) / n)

    def roulette(self):
        a=self.np.array([self.fitness_function(self.decode(x)) for x in self.population_list])
        (t, i) = (self.np.random.random(), 0)
        for p in (a/a.sum()).cumsum():
            if p >= t:
                break
            i = i + 1
        return self.population_list[i]

    def cross_recombination(self,chromosome1,chromosome2):
        p = self.random.random()
        n = 2**self.chromosome_size-1
        if p<=self.crossover_probability:
            t = self.random.randint (1,self.chromosome_size-1)
            mask = n << t
            (r1, r2) = (chromosome1 & mask, chromosome2 & mask)
            mask = n >> (self.chromosome_size - t)
            (l1, l2) = (chromosome1 & mask, chromosome2 & mask)
            (chromosome1, chromosome2) = (r1 + l2, r2 + l1)
        return [chromosome1,chromosome2]

    def mutate(self,chromosome):
        p = self.random.random ()
        if p < self.mutation_probability:
            t = self.random.randint(1,self.chromosome_size)
            mask1 = 1 << (t - 1)
            mask2 = chromosome & mask1
            if mask2 > 0:
                chromosome = chromosome & (~mask2)
            else:
                chromosome = chromosome ^ mask1
        return chromosome

    def evolution(self,reproduce_generation=50):
        a=self.np.array(self.population_list)
        b=self.np.array([self.fitness_function(self.decode(x)) for x in a])
        offspring_list=[a[b.argmax()]]
        print(str(0)+'/'+str(reproduce_generation)+'   ','best: ',b.max())
        print(offspring_list)
        print(a)
        for i in range(reproduce_generation):
            for j in range(self.population_size-1):
                offspring_list.append(self.cross_recombination(self.roulette(),self.roulette())[self.random.randint(0,1)])
            offspring_list=[self.mutate(x) for x in offspring_list]
            a=self.np.array(offspring_list)
            b=self.np.array([self.fitness_function(self.decode(x)) for x in a])
            print(str(i+1)+'/'+str(reproduce_generation)+'   ','best: ',b.max())
            print(a)
            print(a[b.argmax()])
            self.population_list=offspring_list[:]
            offspring_list=[a[b.argmax()]]
                
if __name__=='__main__':
    import numpy as np
    def func(x):
        return x*np.sin(10*np.pi*x)+2
    a=Genetic_Algorithm(interval=(-1,2,6),fitness_function=func)
    a.evolution(50)