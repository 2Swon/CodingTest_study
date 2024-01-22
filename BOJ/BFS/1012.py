from collections import deque

n = int(input())
def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < M and 0 <= ny < N and array[nx][ny] == 1:
                que.append((nx, ny))
                array[nx][ny] = 0


for i in range(n):
    M, N, K = map(int, input().split())

    array = [[0 for _ in range(N)] for _ in range(M)]

    for i in range(K):
        a, b = map(int, input().split())
        array[a][b] = 1

    cnt = 0
    for x in range(M):
        for y in range(N):
            if array[x][y] == 1:
                bfs(x, y)
                cnt += 1

    print(cnt)