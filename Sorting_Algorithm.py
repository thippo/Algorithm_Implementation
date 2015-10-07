#writen by thippo
#python version 3.4.3
#reference http://blog.csdn.net/hinyunsin/article/details/6311707

class Sorting_Algorithm():

    def __init__(self,sorting_list):
        assert isinstance(sorting_list,list), 'sorting_list must be list!'
        self.sorting_list=sorting_list[:]
        
    def bubble_sort(self):
        l=len(self.sorting_list)-2
        i=0
        while i<=l:
            j=l
            while j>=i:
                if(self.sorting_list[j+1]<self.sorting_list[j]):
                    self.sorting_list[j],self.sorting_list[j+1]=self.sorting_list[j+1],self.sorting_list[j]
                j-=1
            i+=1
        return self.sorting_list

    def insert_sort(self):
        for i in range(1,len(self.sorting_list)):
            j=i
            while j>0 and self.sorting_list[j-1]>self.sorting_list[i]:
                j-=1
            self.sorting_list.insert(j,self.sorting_list[i])
            self.sorting_list.pop(i+1)
        return self.sorting_list

    def shell_sort(self):
        dist=len(self.sorting_list)//2
        while dist>0:
            for i in range(dist,len(self.sorting_list)):
                tmp=self.sorting_list[i]
                j=i
                while j>=dist and tmp<self.sorting_list[j-dist]:
                    self.sorting_list[j]=self.sorting_list[j-dist]
                    j-=dist
                    self.sorting_list[j]=tmp
            dist//=2
        return self.sorting_list
    
    def quick_sort(self):
        if len(self.sorting_list) <= 1:
            return self.sorting_list
        else:
            p = self.sorting_list[0]
            return Sorting_Algorithm([x for x in self.sorting_list[1:] if x < p]).quick_sort() + [p] + Sorting_Algorithm([x for x in self.sorting_list[1:] if x >= p]).quick_sort()

    def select_sort(self):
        list_length=len(self.sorting_list)
        for i in range(list_length):
            min=i
            for j in range(i+1,list_length):
                if self.sorting_list[min]>self.sorting_list[j]:
                    min=j
            self.sorting_list[min],self.sorting_list[i]=self.sorting_list[i],self.sorting_list[min]
        return self.sorting_list

if __name__=='__main__':
	c=[2,3,5,1,3,6,5]
	a=Sorting_Algorithm(c)
	print(a.select_sort())
