class Node:
    def __init__(self,puzzle,goal):
        self.puzzle=puzzle
        self.goal=goal
        child1=None
        child2=None
        child3=None
        child4=None

    def Index(self,num,p):
        idx=self.p.index(num)
        i= idx//3
        j= idx-(i*3)
        return i,j
    
    def moves(self):
        i0,j0= self.Index('0')
        self.possible_moves(i0,j0)
        
            
    def possible_moves(self,i, j):
        S_moves = []
        possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if 0 <= i + possible_moves[0][0] < 3 and 0 <= j + possible_moves[0][1] < 3:
            S_moves.append(possible_moves[0])
        if 0 <= i + possible_moves[1][0] < 3 and 0 <= j + possible_moves[1][1] < 3:
            S_moves.append(possible_moves[1])
        if 0 <= i + possible_moves[2][0] < 3 and 0 <= j + possible_moves[2][1] < 3:
            S_moves.append(possible_moves[2])
        if 0 <= i + possible_moves[3][0] < 3 and 0 <= j + possible_moves[3][1] < 3:
            S_moves.append(possible_moves[3])
        return S_moves

    def h(self,puzzle,goal):
        hcost=0
        for num in goal:
            ig,jg=self.Index(num,goal)
            ip,jp=self.Index(num,puzzle)
            hcost+=(abs(ig-ip)+abs(jg-jp))
        return hcost

    def child1 (puzzle):#Left
        list_puzzle=list(puzzle)
        index0=puzzle.index('0')
        list_puzzle[index0],list_puzzle[index0-1]=list_puzzle[index0-1],list_puzzle[index0]
        puzzle=str(list_puzzle)
        #call def f?????????
        return puzzle
        
    def child2 (puzzle):#Right
        list_puzzle=list(puzzle)
        index0=puzzle.index('0')
        list_puzzle[index0],list_puzzle[index0+1]=list_puzzle[index0+1],list_puzzle[index0]
        puzzle=str(list_puzzle)
        #call def f?????????
        return puzzle
        
    def child1 (puzzle):#Up
        list_puzzle=list(puzzle)
        index0=puzzle.index('0')
        list_puzzle[index0],list_puzzle[index0-3]=list_puzzle[index0-3],list_puzzle[index0]
        puzzle=str(list_puzzle)
        #call def f?????????
        return puzzle
        
    def child1 (puzzle):#Down
        list_puzzle=list(puzzle)
        index0=puzzle.index('0')
        list_puzzle[index0],list_puzzle[index0+3]=list_puzzle[index0+3],list_puzzle[index0]
        puzzle=str(list_puzzle)
        #call def f?????????
        return puzzle
    

f=Node("35261780","123456780")
print(f.possible_moves(0,0))
