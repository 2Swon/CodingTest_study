from collections import deque
def solution(s):
    answer = True
    stack = deque()
    for i in s:
        if i == '(':
            stack.append('(')

        else:
            if stack:
                stack.popleft()

            else:
                return False

    if stack:
        return False

    return True

print(solution("()()"))