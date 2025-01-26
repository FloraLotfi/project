class Node:
    def __init__(self,puzzle,goal):
        self.puzzle=puzzle
        self.goal=goal
        child1=None
        child2=None
        child3=None
        child4=None

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
            #h=self.h(new_puzzle,self.goal)
            children.append(new_puzzle)
        return children

'''
    def A_star(self):
        startQ=Min_heap()
        startnode=self.puzzle
        g=0
        h=self.h(self.puzzle,self.goal)
        f=g+h
        startQ.insert((f,startnode))
        while startQ.size()>=0:
            cur=startQ.get_min()
            if cur[1]==self.goal:
                pass
            allchild=self.children()
            g+=1
            for ind,i in enumerate(allchild):
                h=self.h(i,self.goal)
                allchild[ind]=(h,i)
            
            for i in allchild:
                pass

  '''          

f=Node("123406785","123456780")
#print(f.possible_moves(0,0))
print(f.children())