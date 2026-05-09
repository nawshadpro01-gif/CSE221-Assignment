import sys
from collections import deque, defaultdict

data = sys.stdin.read().split()
idx = 0

T = int(data[idx]); idx += 1

for _ in range(T):
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    S = int(data[idx]); idx += 1
    D = int(data[idx]); idx += 1

    U = []
    for i in range(M):
        U.append(int(data[idx])); idx += 1

    V = []
    for i in range(M):
        V.append(int(data[idx])); idx += 1

    W = []
    for i in range(M):
        W.append(int(data[idx])); idx += 1

    edges = []
    for i in range(M):
        edges.append((W[i], U[i], V[i]))
    edges.sort(reverse=True)

    parent = []
    for i in range(N + 1):
        parent.append(i)  

    rank = [0] * (N + 1)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  
            x = parent[x]
        return x

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a == root_b:
            return False  
        if rank[root_a] < rank[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        if rank[root_a] == rank[root_b]:
            rank[root_a] += 1
        return True

    tree = defaultdict(list)
    for weight, u, v in edges:
        if union(u, v):
            tree[u].append((v, weight))
            tree[v].append((u, weight))

    if find(S) != find(D):
        print(0)
        continue
    visited = set()
    queue = deque()
    queue.append((S, float('inf')))  

    answer = 0
    while queue:
        node, min_weight_so_far = queue.popleft()

        if node in visited:
            continue
        visited.add(node)

        if node == D:
            answer = min_weight_so_far
            break

        for neighbor, edge_weight in tree[node]:
            if neighbor not in visited:
                new_min = min(min_weight_so_far, edge_weight)
                queue.append((neighbor, new_min))

    print(answer)
