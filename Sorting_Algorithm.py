#writen by thippo
#python version 3.4.3

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

    def heap_sort(self):
        def adjust_heap(lists, i, size):
            lchild = 2 * i + 1
            rchild = 2 * i + 2
            max = i
            if i < size / 2:
                if lchild < size and lists[lchild] > lists[max]:
                    max = lchild
                if rchild < size and lists[rchild] > lists[max]:
                    max = rchild
                if max != i:
                    lists[max], lists[i] = lists[i], lists[max]
                    adjust_heap(lists, max, size)
        def build_heap(lists, size):
            for i in range(0, (size//2))[::-1]:
                adjust_heap(lists, i, size)
        size = len(self.sorting_list)
        build_heap(self.sorting_list, size)
        for i in range(0, size)[::-1]:
            self.sorting_list[0], self.sorting_list[i] = self.sorting_list[i], self.sorting_list[0]
            adjust_heap(self.sorting_list, 0, i)
        return self.sorting_list
        
    def merge_sort(self):
        def merge(left, right):
            i, j = 0, 0
            result = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result += left[i:]
            result += right[j:]
            return result
        def merge_sort_reduce(lists):
            if len(lists) <= 1:
                return lists
            num = len(lists) // 2
            left = merge_sort_reduce(lists[:num])
            right = merge_sort_reduce(lists[num:])
            return merge(left, right)
        self.sorting_list=merge_sort_reduce(self.sorting_list)
        return self.sorting_list

    def radix_sort(self, radix=10):
        import math
        k = int(math.ceil(math.log(max(self.sorting_list), radix)))
        bucket = [[] for i in range(radix)]
        for i in range(1, k+1):
            for j in self.sorting_list:
                bucket[j//(radix**(i-1)) % (radix**i)].append(j)
            del self.sorting_list[:]
            for z in bucket:
                self.sorting_list += z
                del z[:]
        return self.sorting_list

if __name__=='__main__':
    c=[2,3,5,1,3,6,5]
    a=Sorting_Algorithm(c)
    print(a.radix_sort())