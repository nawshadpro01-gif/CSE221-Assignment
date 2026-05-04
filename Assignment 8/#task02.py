import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def unite(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False  # already connected, skip this edge
    if sz[a] < sz[b]:
        a, b = b, a
    parent[b] = a
    sz[a] += sz[b]
    return True  # successfully merged

n, m = map(int, input().split())

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# Sort edges by weight (Kruskal's key step)
edges.sort()

parent = list(range(n + 1))
sz = [1] * (n + 1)

total_cost = 0
edges_used = 0

for w, u, v in edges:
    if unite(u, v):
        total_cost += w
        edges_used += 1
        if edges_used == n - 1:  # MST complete
            break

print(total_cost)