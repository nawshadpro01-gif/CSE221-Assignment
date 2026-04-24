import sys
from collections import deque
input = sys.stdin.readline
n= int(input())
adj = []
for i in range(n+1):
    adj.append([])
for i in range(n-1):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)





def bfs(start, adj, n):
    dist = [-1] * (n + 1)
    dist[start] = 0
    q = deque([start])
    farN = start
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                if dist[v] > dist[farN]:
                    farN = v
    return farN, dist



A, _ = bfs(1, adj, n)
B, dist = bfs(A, adj, n)

print(dist[B])
print(A, B)