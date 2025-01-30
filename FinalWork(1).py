import time
start=time.time()
with open("p.txt", "r") as file:
    content = file.read().split()
N = int(content[0]) 
puzzle = content[1:]
file.close()

def make_goal(num):
    n=(num*num)-1
    x=[]
    for i in range(n):
        x.append(str(i+1))
    x.append(str(0))
    return x

def parent(i):
    return i//2

def left_child(i):
    return 2*i

def right_child(i):
    return 2*i+1
    
class Min_Heap:
    def __init__(self):
        self.heap = [(0,0)] 

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

    def del_min(self) :
        if self.size() == 0 :
            raise Exception("empty list!")
        MIN = self.heap[1]
        self.heap[1] = self.heap[-1]
        del(self.heap[-1])
        self.bubble_down(1)
        return MIN

class Node:
    def __init__(self,puzzle,g,parent,n,move):
        self.puzzle=puzzle
        self.n=n
        self.g=g
        self.f=self.g+self.h(make_goal(self.n))
        self.parent=parent
        self.where=move

    def Index(self,num,p):
        idx=p.index(num)
        i= idx//self.n
        j= idx-(i*self.n)
        return i,j

    def h(self,goal):
        hcost=0
        for num in goal:
            ig,jg=self.Index(num,goal)
            ip,jp=self.Index(num,self.puzzle)
            hcost+=(abs(ig-ip)+abs(jg-jp))
        return hcost
       
    def possible_moves(self,i, j):
        S_moves = []
        possible_moves = {(-1, 0):'Up', (1, 0):'Down', (0, -1):'Left', (0, 1):'Right'}
        for k in possible_moves:
            if (0 <= i + k[0]) and (i+k[0] <= (self.n-1)) and (0 <= j + k[1])and (j +k[1] <= (self.n-1)):
                S_moves.append((k,possible_moves[k]))
        return S_moves
    
    def children(self):
        i0,j0=self.Index('0',self.puzzle)
        possible=self.possible_moves(i0,j0)
        children=[]
        
        for i in possible:
            new_puzzle=list(self.puzzle)
            indx=new_puzzle.index('0')
            new_puzzle[indx],new_puzzle[indx+(i[0][0]*self.n)+i[0][1]]=new_puzzle[indx+(i[0][0]*self.n)+i[0][1]],new_puzzle[indx] 
            if new_puzzle!=self.parent:
                children.append((new_puzzle,i[1]))
        return children

def solvable(puzzle,n):
    inv=0
    line=0
    for indx,i in enumerate(puzzle):
        for j in puzzle[indx+1:]:
            if int(i)!=0 and int(j)!=0 and int(i)>int(j):
                inv+=1
    for j in range(n):
        if '0' in puzzle[j*n:(j+1)*n]:
            line=j%2

    inv=inv%2
    if n%2==1:
        return inv
    else:
        if (line==0 and inv==0)or(line==1 and inv==1):
            return 1
    return 0

def A_star(start_puzzle,goal,n):
    if solvable(start_puzzle,n)==1:
        return 1
    
    startQ=Min_Heap()
    startnode=Node(start_puzzle,0,None,n,None)
    startQ.insert((startnode.f,startnode))
    closed=[]

    while startQ.size()>=0:
        f,cur=startQ.del_min()
        
        if cur.puzzle==goal:
            return (cur,n)
        
        closed.append(cur.puzzle)

        allchildren=cur.children()
        
        for i in allchildren:
            if i[0] in closed:
                continue
            new_child=Node(i[0],cur.g+1,cur,n,i[1])
            startQ.insert((new_child.f,new_child))
    return None

def Print(result):
    if result==1:
        print('puzzle is not sovable!')
        return 
    
    cur=result[0]
    n=int(result[1])
    path=[]
    
    while cur:
        path.append(cur)
        cur = cur.parent
    
    path=path[::-1]
    k=-1
    for i in path:
        k+=1
        if k!=0:
            print("step",k,":",i.where)#,"\n") 
        #'''
        for m in range(n):
            for j in i.puzzle[m*n:(m+1)*n]:
                print(j,end=' ')
            print('')
        #'''
    print('total number of steps:',k)
         
f=A_star(puzzle,make_goal(N),N)
Print(f)
end=time.time()
total_time= end - start
print(total_time)