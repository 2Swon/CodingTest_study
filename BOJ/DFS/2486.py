import sys
sys.setrecursionlimit(10**5)
N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

min_h = min(map(min, graph))
max_h = max(map(max, graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, h):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
            if graph[nx][ny] > h:
                visited[nx][ny] = True
                dfs(nx, ny, h)

result = 0

for i in range(min_h -1, max_h):
    visited = [[False]*N for _ in range(N)]
    cnt = 0

    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == False:
                dfs(j, k, i)
                cnt += 1

    result = max(result, cnt)

print(result)