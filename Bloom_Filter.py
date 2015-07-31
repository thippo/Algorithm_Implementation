#writen by thippo
#python version 3.4.3
#reference http://blog.csdn.net/demon24/article/details/8537665    

class BloomFilter():
    
    import BitVector
    
    class SimpleHash():  

        def __init__(self, cap, seed):
            self.cap = cap
            self.seed = seed

        def hash(self, value):
            ret = 0
            for i in range(len(value)):
                ret += self.seed*ret + ord(value[i])
            return (self.cap-1) & ret

    def __init__(self,bit_size=25,hash_count=7):
        self.bit_size = 1 << bit_size
        self.seeds = list(range(hash_count))
        self.bitset = self.BitVector.BitVector(size=self.bit_size)
        self.hashfunction = []
        
        for i in range(len(self.seeds)):
            self.hashfunction.append(self.SimpleHash(self.bit_size, self.seeds[i]))
   
    def insert(self, value):
        for f in self.hashfunction:
            loc = f.hash(value)
            self.bitset[loc] = 1
			
    def lookup(self, value):
        if value == None:
            return False
        ret = True
        for f in self.hashfunction:
            loc = f.hash(value)
            ret = ret & self.bitset[loc]
        return ret

def main():
    a=iter(['a','b','c','a'])
    bloomfilter = BloomFilter(bit_size=10,hash_count=5)
    while True:
        try:
            url = a.__next__()
        except StopIteration:
            break
        if bloomfilter.lookup(url) == False:
            bloomfilter.insert(url)
            print('%s has not exist and insert' % url)
        else:
            print ('%s has exist' % url )
            
main()