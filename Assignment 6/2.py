import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

adj = []
for i in range(n+1):
    adj.append([])
    

for i in range(m):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)


color = [-1] * (n+1)

ans = 0

for i in range(1, n+1):
    if color[i] == -1:
        q = deque([i])
        color[i] = 0
        count = [1,0]

        while q:
            u = q.popleft()
            for i in adj[u]:
                if color[i] == -1:
                    color[i] = 1-color[u]
                    count[color[i]] +=1 
                    q.append(i)

        ans += max(count)

print(ans)
