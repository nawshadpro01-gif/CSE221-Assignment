import sys 
from collections import deque

input= sys.stdin.readline

n = int(input())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

move=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]



dist = [[-1] * n for i in range(n)]

q = deque()
q.append((x1,y1))
dist[x1][y1] = 0

while q:
    x,y = q.popleft()

    if(x,y) == (x2,y2):

            break 
    

    for dx,dy in move:
        nx,ny= x+dx,y+dy
        if 0 <= nx < n and 0 <= ny < n and dist[nx][ny]==-1:
            dist[nx][ny]= dist[x][y] + 1
            q.append((nx,ny))
print(dist[x2][y2])