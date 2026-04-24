#task 5
import sys
from collections import deque
input = sys.stdin.readline
n, m, s, q = map(int, input().split())
adj = []
for i in range(n+1):
    adj.append([])
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)



s = list(map(int,input().split()))
d = list(map(int,input().split()))
dist = [-1] * (n + 1)
q = deque()

for i in s:
    dist[i] = 0
    q.append(i)

while q:
    u=q.popleft()
    for v in adj[u]:
        if dist[v]==-1:
            dist[v]=dist[u]+1
            q.append(v)
for i in d:
    print(dist[i], end=' ')
