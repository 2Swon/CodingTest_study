def solution(n, computers):
    answer = 0
    visited = [False]*n

    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i, visited)
            answer += 1

    return answer

def dfs(n, computers, v, visited):
    visited[v] = True
    for con in range(n):
        if con != v and computers[v][con] == 1:
            if visited[con] == False:
                dfs(n, computers, con, visited)

from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1
    return answer

def BFS(n, computers, com, visited):
    visited[com] = True
    queue = []
    queue.append(com)
    while len(queue) != 0:
        com = queue.pop(0)
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[com][connect] == 1:
                if visited[connect] == False:
                    queue.append(connect)