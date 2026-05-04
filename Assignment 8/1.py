import sys 
input = sys.stdin.readline

n,k=map(int,input().split())

p = list(range(n+1))
sL = [1]*(n+1)

def find(x):
    if p[x] != x:
        p[x] =find(p[x])

    return p[x]

def union(a,b):
    ra = find(a)
    rb = find(b) 

    if ra != rb:
        if sL[ra] < sL[rb]:
            ra,rb = rb,ra
        p[rb] =ra
        sL[ra] +=sL[rb]
    
    return sL[find(ra)]




for i in range(k):
    a,b = map(int,input().split())
    print(union(a,b))