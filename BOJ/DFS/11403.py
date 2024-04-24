from collections import deque

N = int(input())

graph = []

for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)


res_graph = [[0] * N for _ in range(N)]


def bfs(v):
    que = deque()
    que.append(v)
    visited = [False] * N
    while que:
        a = que.popleft()

        for i in range(N):
            if not visited[i] and graph[a][i] == 1:
                que.append(i)
                visited[i] = True
                res_graph[v][i] = 1


for j in range(N):
    bfs(j)

for i in res_graph:
    print(*i)