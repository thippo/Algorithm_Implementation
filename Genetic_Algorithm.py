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
        self.population_list=[self.generate_chromosome() for x in range(self.population_size)]
    
    def encode_length(self):
        i=0
        while (self.interval[1]-self.interval[0])*10**self.interval[2] > 2**i: i+=1
        return i

    def generate_chromosome(self):
        return ''.join([str(self.random.randint(0,1)) for x in range(self.chromosome_size)])

    def decode(self,chromosome):
        n =  2 ** self.chromosome_size -1
        return (self.interval[0] + int(chromosome,2) * (self.interval[1]-self.interval[0]) / n)

    def roulette(self):
        a=self.np.array([self.fitness_function(self.decode(x)) for x in self.population_list])
        (t, i) = (self.np.random.random(), 0)
        for p in (a/a.sum()).cumsum():
            if p >= t:
                break
            i = i + 1
        return i
    
    def cross_recombination(self,chromosome1,chromosome2):
        p = self.random.random()
        if p <= self.crossover_probability:
            t=self.random.randint(1,self.chromosome_size-1)
            tmp1=chromosome1[t:]
            tmp2=chromosome2[t:]
            chromosome1=chromosome1[:t]+tmp2
            chromosome2=chromosome2[:t]+tmp1
        return [chromosome1,chromosome2]
            
    def mutate(self,chromosome):
        p = self.random.random()
        chromosome_list=list(chromosome)
        if p <= self.mutation_probability:
            t=self.random.randint(0,self.chromosome_size-1)
            chromosome_list[t]={'0':'1','1':'0'}[chromosome_list[t]]
        return ''.join(chromosome_list)
    
    def evolution(self,reproduce_generation=50):
        print(str(0)+'/'+str(reproduce_generation)+'   ',end='')
        offspring_list=[self.population_list[self.np.array([self.fitness_function(self.decode(x)) for x in self.population_list]).argmax()]]
        print('best: ',self.np.array([self.fitness_function(self.decode(x)) for x in self.population_list]).max())
        for i in range(reproduce_generation):
            offspring_list.append(self.population_list[self.np.array([self.fitness_function(self.decode(x)) for x in self.population_list]).argmax()])
            for j in range(self.population_size-1):
                chromosome_cross=self.random.sample(self.population_list,2)
                offspring_list.append(self.cross_recombination(chromosome_cross[0],chromosome_cross[1])[0])
                offspring_list.append(self.cross_recombination(chromosome_cross[0],chromosome_cross[1])[1])
            offspring_list=[self.mutate(x) for x in offspring_list]
            print(str(i+1)+'/'+str(reproduce_generation)+'   ',end='')
            print('best: ',self.np.array([self.fitness_function(self.decode(x)) for x in offspring_list]).max())
            self.population_list=offspring_list[:]
            offspring_list=[]
            
if __name__=='__main__':
    import numpy as np
    def func(x):
        return x*np.sin(10*np.pi*x)+2
    a=Genetic_Algorithm(interval=(-1,2,6),fitness_function=func)
    a.evolution(200)