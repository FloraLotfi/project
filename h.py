def man_h(puzzle,num):
    i1,j1=ij("123456780",num)
    i0,j0=ij(puzzle,num)
    i=abs(i1-i0)
    j=abs(j1-j0)
    return i+j

def ij(puzzle,num):
    indx=puzzle.index(num)
    i=indx//3
    j=indx-(i*3)
    return i,j