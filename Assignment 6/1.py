import sys 
from collections import deque

input = sys.stdin.readline 

T = int(input())
for i in range(T):
    n,m = map(int, input().split())

    adj = []
    for _ in range(n + 1):
        adj.append([])

    indeg = [0] *(n+1) 

    for i in range(m):
        a,b = map(int,input().split())
        adj[a].append(b)
        indeg[b] +=1 

    q = deque()
    for i in range(1,n+1):
        if indeg[i] == 0:
            q.append(i)

    result = []
    while q: 
        node = q.popleft()
        result.append(node)

        for i in adj[node]:
            indeg[i] -=1

            if indeg[i] == 0:
                q.append(i)
        
    if len(result) != n:
            print(-1)
    else:
            print(*result)

