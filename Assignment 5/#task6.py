import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

subtree = [0] * (N + 1)

def dfs(node, parent):
    size = 1
    for nxt in graph[node]:
        if nxt != parent:
            size += dfs(nxt, node)
    subtree[node] = size
    return size

dfs(R, -1)

Q = int(input())
for _ in range(Q):
    x = int(input())
    print(subtree[x])