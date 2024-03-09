from collections import deque

N, M, V = map(int, input().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [False for _ in range(N+1)]
visited2 = visited.copy()

ans = []
ans2 = []
def dfs(v):
    visited[v] = True
    ans.append(v)
    for i in range(N+1):
        if graph[v][i] == 1 and visited[i] == False:
            dfs(i)

def bfs(v):
    visited2[v] = True
    que = deque([v])

    while que:
        V = que.popleft()
        ans2.append(V)
        for i in range(N+1):
            if graph[V][i] == 1 and visited2[i] == False:
                que.append(i)
                visited2[i] = True


dfs(V)
print(*ans)
bfs(V)
print(*ans2)
