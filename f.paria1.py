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
        self.heap[1] = self.heap[-1]
        del(self.heap[-1])
        self.bubble_down(1)
        return MIN





class Node:
    def __init__(self,puzzle,goal,g,parent):
        self.puzzle=puzzle
        self.goal=goal
        self.g=g
        self.parent=parent
        

    def Index(self,num,p):
        idx=p.index(num)
        i= idx//3
        j= idx-(i*3)
        return i,j
    
    def moves(self):
        i0,j0= self.Index('0')
        self.possible_moves(i0,j0)
        
            
    def possible_moves(self,i, j):
        S_moves = []
        possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for k in possible_moves:
            if (0 <= i + k[0]) and (i+k[0] < 3) and (0 <= j + k[1])and (j +k[1] < 3):
                S_moves.append(k)
        return S_moves

    def h(self,puzzle,goal):
        hcost=0
        for num in goal:
            ig,jg=self.Index(num,goal)
            ip,jp=self.Index(num,puzzle)
            hcost+=(abs(ig-ip)+abs(jg-jp))
        return hcost

    def children(self):
        i0,j0=self.Index('0',self.puzzle)
        possible=self.possible_moves(i0,j0)
        children=[]
        for i in possible:
            new_puzzle=list(self.puzzle)
            indx=new_puzzle.index('0')
            new_puzzle[indx],new_puzzle[indx+(i[0]*3)+i[1]]=new_puzzle[indx+(i[0]*3)+i[1]],new_puzzle[indx] 
            new_puzzle=''.join(new_puzzle)
            if new_puzzle!=self.parent:
                children.append(new_puzzle)
        childrenobject=[]
        for i in children:
            childrenobject.append(Node(i,self.goal,self.g+1,self))
        for i in childrenobject:
            print(i.puzzle)
        return childrenobject


    def A_star(self):
        startQ=Min_Heap()
        startnode=Node(self.puzzle,self.goal,0,None)
        h=self.h(self.puzzle,self.goal)
        f=self.g+h
        startQ.insert((f,startnode))
        visit=set()

        while startQ.size()>=0:
            f,cur=startQ.del_min()

            if cur.puuzle==self.goal:
                print("we are here!")

            allchild=cur.children()
            g+=1
            for ind,i in enumerate(allchild):
                h=self.h(i.puzzle,self.goal)
                allchild[ind]=(h+g,i)
                if 
            
            for i in allchild:
                pass

         

f=Node("123406785","123456780",0,"103426785")
#print(f.possible_moves(0,0))
print(f.children())