from collections import deque
import sys
input = sys.stdin.readline

def solve():
    line1 = input().split()
    N, M, S, D = int(line1[0]), int(line1[1]), int(line1[2]), int(line1[3])

    # Build adjacency list
    adj = [[] for _ in range(N + 1)]

    if M > 0:
        us = list(map(int, input().split()))
        vs = list(map(int, input().split()))
        for u, v in zip(us, vs):
            adj[u].append(v)
            adj[v].append(u)
    else:
        # consume empty lines if present
        input()
        input()

    # Sort adjacency lists so we can greedily pick smallest neighbor
    for i in range(N + 1):
        adj[i].sort()

    # Edge case: source == destination
    if S == D:
        print(0)
        print(S)
        return

    # Phase 1: BFS from destination to compute dist_to_dest for every node
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[D] = 0
    queue = deque([D])

    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if dist[neighbor] == INF:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    # No path exists
    if dist[S] == INF:
        print(-1)
        return

    # Phase 2: Greedy path reconstruction from S to D
    # At each step, pick the smallest neighbor that is exactly 1 step closer to D
    path = [S]
    current = S

    while current != D:
        best = -1
        for neighbor in adj[current]:
            if dist[neighbor] == dist[current] - 1:
                best = neighbor  # adj is sorted, so first valid = smallest
                break
        path.append(best)
        current = best

    print(dist[S])
    print(*path)

solve()