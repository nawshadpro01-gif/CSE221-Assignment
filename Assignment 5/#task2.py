import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def ques():
    n, m = map(int, input().split())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))

    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        adj[u[i]].append(v[i])
        adj[v[i]].append(u[i])
    
    for i in range(1, n + 1):
        adj[i].sort(reverse=True)  # Reverse so smallest pops first from stack

    color = [0] * (n + 1)
    order = []
    
    stack = [1]
    while stack:
        node = stack.pop()
        if color[node]:
            continue
        color[node] = 1
        order.append(node)
        for neighbor in adj[node]:
            if not color[neighbor]:
                stack.append(neighbor)
    
    print(*order)

ques()