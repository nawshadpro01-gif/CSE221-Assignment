import sys
input = sys.stdin.readline

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # path compression
        x = parent[x]
    return x

def main():
    n, m, q = map(int, input().split())
    
    parent = list(range(n + 1))
    
    for _ in range(m):
        u, v = map(int, input().split())
        pu, pv = find(parent, u), find(parent, v)
        if pu != pv:
            parent[pu] = pv  # union
    
    for _ in range(q):
        x, y = map(int, input().split())
        print("YES" if find(parent, x) == find(parent, y) else "NO")

main()