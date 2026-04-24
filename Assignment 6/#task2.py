import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

color = [-1] * (n + 1)
ans = 0

for i in range(1, n + 1):
    if color[i] == -1:
        q = deque([i])
        color[i] = 0
        cnt = [1, 0]

        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    cnt[color[v]] += 1
                    q.append(v)

        ans += max(cnt)

print(ans)