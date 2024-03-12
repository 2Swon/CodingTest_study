R, C = map(int, input().split())

graph = []

for _ in range(R):
    graph.append(list(map(str, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0
def dfs(x, y):
    global ans
    ans = max(ans, len(visited))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] not in visited:
                visited.add(graph[nx][ny])
                dfs(nx, ny)
                visited.remove(graph[nx][ny])
    return ans

visited = set()
visited.add(graph[0][0])

print(dfs(0, 0))

