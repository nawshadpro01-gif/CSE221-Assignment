#task 5
import sys
from collections import deque

input = sys.stdin.readline

n, m, s, q = map(int, input().split())

adj = []
for i in range(n+1):
    adj.append([])

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

sources = list(map(int, input().split()))
dest = list(map(int, input().split()))

dist = [-1] * (n + 1)

queue = deque()

# multi-source start
for src in sources:
    dist[src] = 0
    queue.append(src)

while queue:
    u = queue.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            queue.append(v)

print(*[dist[d] for d in dest])