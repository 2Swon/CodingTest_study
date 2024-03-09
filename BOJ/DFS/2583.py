M, N, K = map(int, input().split())

graph = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    global count

    if x < 0

