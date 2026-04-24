import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(start):
    dist = [-1] * (n + 1)
    q = deque([start])
    dist[start] = 0

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)

    farthest = start
    for i in range(1, n + 1):
        if dist[i] > dist[farthest]:
            farthest = i

    return farthest, dist[farthest]

# first BFS
A, _ = bfs(1)

# second BFS
B, diameter = bfs(A)

print(diameter)
print(A, B)