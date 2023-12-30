from collections import deque
row, column = map(int, input().split())

graph = []

for _ in range(row):
    graph.append(list(map(int, input().split())))
def bfs(x, y):
    graph[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque([(x,y)])
    cnt = 1
    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < column and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                que.append((nx, ny))
    return cnt

max_size = 0
ans = 0
for i in range(row):
    for j in range(column):
        if graph[i][j] == 1:
            ans += 1
            max_size = max(max_size, bfs(i, j))

print(ans)
print(max_size)



