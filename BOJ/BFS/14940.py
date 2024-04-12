from collections import deque

N, M = map(int, input().split())

graph = []

target_x, target_y = 0, 0

for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    if 2 in data:
        target_x, target_y = i, data.index(2)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0

que = deque()
que.append([target_x, target_y])

visited = [[False] * M for _ in range(N)]
visited[target_x][target_y] = True

ans = [[0] * M for _ in range(N)]

def bfs():
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if graph[nx][ny] == 1:
                        ans[nx][ny] = ans[x][y] + 1
                        visited[nx][ny] = True
                        que.append((nx, ny))



bfs()

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 1:
            print(-1, end=" ")

        else:
            print(ans[i][j], end=" ")

    print()