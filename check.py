s={0:0,1:'e',2:'t'}
for i in s:
    pass
#s.append(j:l)
print(s)
j=[0,(1,'k'),(5,'l'),(9,'o')]
print(j[1][0])

g=0
allchild=[(1,'k'),(5,'l'),(9,'o')]

allchild[0]=allchild[1]
for i in allchild:
    pass
print(allchild)

def Index(num,p):
    idx=p.index(num)
    i= idx//3
    j= idx-(i*3)
    return i,j

def h(puzzle,goal):
    hcost=0
    for num in goal:
        ig,jg=Index(num,goal)
        ip,jp=Index(num,puzzle)
        hcost+=(abs(ig-ip)+abs(jg-jp))
    return hcost


print(h('123840765','123456780'))