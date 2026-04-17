import sys 
input = sys.stdin.readline

def search(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def solN():
    n,m,q = map(int,input().split())

    parent = []
    for i in range(n+1):
        parent.append(i)

    for i in range(m):
        u,v = map(int,input().split())
        pu = search(parent,u)
        pv = search(parent,v)
        if pu != pv:
            parent[pu] = pv

    for i in range(q):
        x,y = map(int,input().split())
        if search(parent, x) == search(parent,y):
            print("YES")
        else:
            print("NO")

solN()