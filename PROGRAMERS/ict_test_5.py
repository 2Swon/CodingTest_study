from collections import deque


def countMatches(grid1, grid2):
    cnt = 0
    same = 1

    que = deque()

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited = [[False for _ in range(len(grid1))] for _ in range(len(grid1))]

    for i in range(len(grid1)):
        for j in range(len(grid1)):
            if visited[i][j] == False and grid1[i][j] == '1' and grid2[i][j] == '1':
                que.append((i, j))
                same = 1
                while (que):
                    y, x = que.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < len(grid1) and 0 <= ny < len(grid1):
                            if visited[ny][nx] == False:
                                if grid1[ny][nx] == '1' and grid2[ny][nx] == '1':
                                    que.append((ny, nx))
                                    visited[ny][nx] = True

                                elif grid1[ny][nx] == '1' or grid2[ny][nx] == '1':
                                    same = 0
                if same == 1:
                    cnt += 1

    return cnt
