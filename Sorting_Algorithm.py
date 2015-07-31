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

            
c=[2,3,5,1,3,6,5,7,2,9,4]
a=Sorting_Algorithm(c)