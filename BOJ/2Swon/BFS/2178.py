from collections import deque
row, column = map(int, input().split())

graph = []

for _ in range(row):
    graph.append(list(map(int, input())))
def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque()

    que.append((x,y))
    while(que):
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < column and graph[nx][ny] == 1:
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[row-1][column-1]


print(bfs(0,0))

