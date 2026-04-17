from collections import deque
import sys
input = sys.stdin.readline

def ques():
    n,m,s,d = map(int,input().split())

    adj = []
    for i in range(n+1):
        adj.append([])

    if m > 0:
        U=list(map(int,input().split()))
        V=list(map(int,input().split()))
        for u,v in zip(U,V):
            adj[u].append(v)
            adj[v].append(u)

    for i in range(n+1):
        adj[i].sort()
        
    if s == d:
        print(0)
        print(s)
        return
    not_visited = False 
    dist = [-1] * (n+1)
    dist[d] = 0
    q = deque([d])

    while q:
        node = q.popleft()
        for i in adj[node]:
            if dist[i] == 0:
                dist[i] = dist[node] +1 
                q.append(i)

    if dist[s] == -1:
        print(-1)
        return
    
    path =[s]
    current = s


    while current!=d:
        b = 0  # placeholder
        for i in adj[current]:
            if dist[i] == dist[current] -1:
                b = i
                break 
        path.append(b)
        current = b

    print(dist[s])
    print(*path)

ques()

