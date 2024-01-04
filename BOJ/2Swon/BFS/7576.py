from collections import deque

N, M = map(int, input().split())

graph = []
que = deque([])
ans = 0        

for _ in range(M):
    graph.append(list(map(int,input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            que.append((i, j))

def bfs():
    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
                que.append((nx, ny))
                graph[nx][ny] = graph[a][b] + 1

bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    
    ans = max(ans, max(i))

print(ans-1)



