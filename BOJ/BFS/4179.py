from collections import deque

R, C = map(int, input().split())

maze = []
for _ in range(R):
    maze.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

jx, jy = 0, 0
fire_queue = deque()
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            jx, jy = i, j
        elif maze[i][j] == 'F':
            fire_queue.append((i, j))

jqueue = deque()
jqueue.append((jx, jy, 0))

while jqueue:
    for _ in range(len(fire_queue)):
        fx, fy = fire_queue.popleft()
        for i in range(4):
            nfx, nfy = fx + dx[i], fy + dy[i]
            if 0 <= nfx < R and 0 <= nfy < C and maze[nfx][nfy] == '.':
                maze[nfx][nfy] = 'F'
                fire_queue.append((nfx, nfy))

    for _ in range(len(jqueue)):
        x, y, cnt = jqueue.popleft()
        if x == 0 or x == R-1 or y == 0 or y == C-1:
            print(cnt + 1)
            exit(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] == '.':
                maze[nx][ny] = 'J'
                jqueue.append((nx, ny, cnt + 1))

print("IMPOSSIBLE")