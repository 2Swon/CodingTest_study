from collections import deque

def solution(numbers, target):

    que = deque()
    que.append([numbers[0], 0])
    que.append([-1*numbers[0], 0])
    answer = 0
    while que:
        num, idx = que.popleft()
        idx += 1
        if idx < len(numbers):
            que.append([num + numbers[idx], idx])
            que.append([num - numbers[idx], idx])

        else:
            if num == target:
                answer += 1

    return answer

print(solution([1, 1, 1, 1, 1], 3))