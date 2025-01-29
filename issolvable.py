def check(puzzle):#, goal,num):
    inv=0
    for indx,i in enumerate(puzzle):
        for j in puzzle[indx+1:]:
            if int(i)!=0 and int(j)!=0 and int(i)>int(j):
                inv+=1
    return inv%2
