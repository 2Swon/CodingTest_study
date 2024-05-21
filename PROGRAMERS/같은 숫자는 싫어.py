from collections import deque
def solution(arr):
    que = deque(arr)
    ans = [que[0]]
    for i in range(len(que)):
        a = que.popleft()
        if a != ans[-1] and i != 0:
            ans.append(a)
    return ans

print(solution([4,4,4,3,3]))

