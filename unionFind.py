#Union-Find implementation Module
# This data structure can be used to store non-overlapping subsets of elements

class union_find: #using weighted quick union by rank with path compression
    
    def __init__(self, n):#Initialize an empty union-find object with n items
        self._id = list(range(n))
        self._count = n
        self._rank = [0] * n
    
    def find(self, l): # Find which set l belongs
        id = self._id
        while l != id[l]:
            l = id[l] = id[id[l]]   # Path compression using halving
        return l
    
    def count(self): #Counts the number of elements
        return self._count
    
    def connected(self, l1, l2): #Check connectivity of l1 and l2 (do l1 and l2 belong to the same set or not)
        return self.find(l1) == self.find(l2)
    
    def union(self, l1, l2): #Union of l1 and l2 using rank (always attaching the smaller tree to the larger tree)
        id = self._id
        rank = self._rank
        i = self.find(l1)
        j = self.find(l2)
        if i == j:
            return
        self._count -= 1
        if rank[i] < rank[j]:
            id[i] = j
        elif rank[i] > rank[j]:
            id[j] = i
        else:
            id[j] = i
            rank[i] += 1