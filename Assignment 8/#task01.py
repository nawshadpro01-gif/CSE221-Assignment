import sys
input = sys.stdin.readline

N, K = map(int, input().split())

parent = list(range(N + 1))
size = [1] * (N + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # path compression
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)
    
    if ra != rb:
        # union by size
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        
        parent[rb] = ra
        size[ra] += size[rb]
    
    return size[find(ra)]

for _ in range(K):
    a, b = map(int, input().split())
    print(union(a, b))