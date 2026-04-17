from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    n,m= map(int, input().split())
    adj = []
    for i in range(n+1):
        adj.append([])

    for i in range(m):
        u,v= map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)

    for i in range(1,n+1):
        adj[i].sort()

    color = [0] *(n+1)
    ord = []

    q = deque()
    color[1]= 1
    q.append(1)
    while q:
        u = q.popleft()
        ord.append(u)
        for v in adj[u]:
            if color[v] == 0:
                color[v] = 1
                q.append(v)
    print(*ord)

bfs()
