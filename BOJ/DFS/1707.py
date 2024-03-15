def solution():
    V, E = map(int, input().split())

    visited = [False]*(V+1)
    graph = [[]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    def dfs(start, group)

solution()