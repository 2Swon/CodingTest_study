from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    que = deque()
    que.append([0, 0])
    while que:
        y, x = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    que.append([ny, nx])
                    visited[ny][nx] = True
                    maps[ny][nx] = maps[y][x] + 1

    answer = maps[n-1][m-1]

    if answer == 1:
        return -1

    else:
        return answer



print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
