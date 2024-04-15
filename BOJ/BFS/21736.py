from collections import deque

N, M = map(int, input().split())

graph = []

for i in range(N):
    data = list(input())
    graph.append(data)

    for j in data:
        if j == 'I':
            x, y = i, data.index(j)

visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0


def bfs(a, b):
    que = deque()
    que.append([a, b])
    visited[a][b] = True
    global cnt

    while que:
        aa, bb = que.popleft()

        for i in range(4):
            nx = aa + dx[i]
            ny = bb + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if not graph[nx][ny] == 'X' and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = True

                    if graph[nx][ny] == 'P':
                        cnt += 1

bfs(x, y)

if cnt == 0:
    print('TT')

else:
    print(cnt)