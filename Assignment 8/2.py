import sys
input = sys.stdin.readline

def find(x):
    while p[x] !=x:
        p[x] =p[p[x]]
        x =p[x]
    return x
def unite(a, b):
    a,b=find(a),find(b)
    if a ==b:
        return False  
    if sL[a] <sL[b]:
        a,b=b,a
    p[b] =a
    sL[a] +=sL[b]
    return True





n, m =map(int,input().split())
ed =[]
for i in range(m):
    u,v,w =map(int,input().split())
    ed.append((w,u,v))
ed.sort()

p=list(range(n+1))
sL =[1] *(n +1)
t_Cost =0
ed_Used =0
for w,u,v in ed:
    if unite(u,v):
        t_Cost+= w
        ed_Used+=1
        if  ed_Used== n-1:
            break

print(t_Cost)