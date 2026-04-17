import sys
from collections import deque

input = sys.stdin.readline

N, M, S, D, K = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)


def bfs(start, end):
    parent = [-1] * (N + 1)
    q = deque([start])
    parent[start] = start

    while q:
        node = q.popleft()

        if node == end:
            break

        for nxt in graph[node]:
            if parent[nxt] == -1:
                parent[nxt] = node
                q.append(nxt)

    if parent[end] == -1:
        return None

    # reconstruct path
    path = []
    cur = end
    while cur != parent[cur]:
        path.append(cur)
        cur = parent[cur]
    path.append(start)
    path.reverse()

    return path


# path S -> K
path1 = bfs(S, K)

# path K -> D
path2 = bfs(K, D)

if path1 is None or path2 is None:
    print(-1)
else:
    full_path = path1 + path2[1:]
    print(len(full_path) - 1)
    print(*full_path)