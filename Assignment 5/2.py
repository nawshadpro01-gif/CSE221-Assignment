import sys
sys.setrecursionlimit(2*100000 +5)
input = sys.stdin.readline

def ques():
    n,m= map(int, input().split())
    u = list(map(int, input().split()))
    v = list(map(int,input().split()))

    adj = []
    for i in range(n+1):
        adj.append([])

    for i in range(m):
        adj[u[i]].append(v[i])
        adj[v[i]].append(u[i])
    for i in range(1,n+1):
        adj[i].sort(reverse = True )


    color = [0]* (n+1)
    order = []

    # def dfs(node):
    #     color[node] = 1
    #     order.append(node)
    #     for i in adj[node]:
    #         if not color[i]:
    #             dfs(i)

    stack = [1]
    while stack:
        node = stack.pop()
        if color[node]:
            continue
        color[node] = 1
        order.append(node)
        for i in adj[node]:
            if not color[i]:
                stack.append(i)
    print(*order)
ques()