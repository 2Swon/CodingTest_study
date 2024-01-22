from collections import deque

i = int(input())

def bfs(a, b, x, y, N):
    que = deque([(a, b)])
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    array = [[0 for _ in range(N)] for _ in range(N)]

    while que:
        a, b = que.popleft()

        if a == x and b == y:
            return array[a][b]
        for i in range(8):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0 <= nx < N and 0 <= ny < N and array[nx][ny] == 0:
                array[nx][ny] = array[a][b] + 1
                que.append((nx, ny))

    return array


for _ in range(i):
    N = int(input())
    a, b = map(int, input().split())
    x, y = map(int, input().split())
    print(bfs(a, b, x, y, N))
