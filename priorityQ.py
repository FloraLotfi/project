#heap

def parent(i):
    return i//2

def left_child(i):
    return 2*i

def right_child(i):
    return 2*i+1
    
class Min_Heap:
    def __init__(self):
        self.heap = [(0,0)] #the zero'th is redundant
  
    def size(self):
        return len(self.heap)-1
    
    def bubble_down(self,ind): 
        while left_child(ind) <= self.size():
            newInd = ind
            if self.heap[left_child(ind)][0] < self.heap[ind][0]:
                    newInd = left_child(ind)
            if right_child(ind) <= self.size() and self.heap[right_child(ind)][0] < self.heap[newInd][0]:
                    newInd = right_child(ind)
            if ind == newInd:
                    break
            self.heap[ind], self.heap[newInd] = self.heap[newInd], self.heap[ind]
            ind = newInd
    
    def bubble_up(self,ind):
        while ind > 1 and self.heap[ind][0] < self.heap[parent(ind)][0] :
            self.heap[ind], self.heap[parent(ind)] = self.heap[parent(ind)], self.heap[ind]
            ind = parent(ind)

    def insert(self, item):
        self.heap.append(item)
        self.bubble_up(self.size())
        
    def get_min(self) :
        if self.size() == 0 :
            raise Exception("Heap is empty")
        return self.heap[1]

    def del_min(self) :
        if self.size() == 0 :
            raise Exception("Heap is empty")
        MIN = self.heap[1]
        self.heap[1] = self.heap[-1]s
        del(self.heap[-1])
        self.bubble_down(1)
        return MIN


