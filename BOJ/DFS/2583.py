import sys
sys.setrecursionlimit(10**5)

M, N, K = map(int, input().split())

graph = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] = 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, cnt):
    graph[x][y] = 1

    for i in range(4):
        X = x+ dx[i]
        Y = y+ dy[i]

        if 0 <= X < M and 0 <= Y < N:
            if graph[X][Y] == 0:
                cnt = dfs(X, Y, cnt+1)

    return cnt

ans = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            ans.append(dfs(i, j, 1))

print(len(ans))
print(*sorted((ans)))

