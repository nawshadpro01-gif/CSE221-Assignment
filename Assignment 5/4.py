from collections import deque
import sys
input = sys.stdin.readline

n,m,s,d,k = map(int, input().split())

graph = []
for i in range(n+1):
    graph.append([])
for i in range(m):

    u,v = map(int,input().split())
    graph[u].append(v)

def bfs(start,end):
    parent = [-1] *(n+1)
    q = deque([start])
    parent[start] = start


    while q:
        node = q.popleft()
        if node == end:
            break
        for i in graph[node]:
            if parent[i] == -1:
                parent[i] = node
                q.append(i)
    if parent[end] == -1: 
        return None
    




    path = []
    current = end 
    while current != parent[current]: 
        path.append(current) 
        current = parent[current] 
    path.append(start) 
    path.reverse()
    return path


#path1
path1 = bfs(s,k)

#path2 
path2 =bfs(k,d)

if path1 is None or path2 is None:
    print(-1)

else:
    path_T = path1 + path2[1:]
    print(len(path_T)-1)
    print(*path_T)