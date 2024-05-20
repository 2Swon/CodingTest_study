# from collections import deque
# def solution(numbers, target):
#     answer = 0
#
#     que = deque()
#     que.append([numbers[0], 0])
#     que.append([-1 * numbers[0], 0])
#
#     while que:
#         num, idx = que.popleft()
#
#         if idx < len(numbers)-1:
#             que.append([num + numbers[idx + 1], idx + 1])
#             que.append([num - numbers[idx + 1], idx + 1])
#
#         else:
#             if num == target:
#                 answer += 1
#
#     return answer
#
#
# print(solution([1, 1, 1, 1, 1], 3))

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i, visited)
            answer += 1

    return answer
def dfs(n, computers, v, visited):
    visited[v] = True
    for con in range(n):
        if con != v and computers[v][con] == 1:
            if not visited[con]:
                dfs(n, computers, con, visited)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))