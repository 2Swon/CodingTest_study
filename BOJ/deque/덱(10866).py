from collections import deque
import sys
n = int(sys.stdin.readline())

stack = deque()

for _ in range(n):
    s = sys.stdin.readline().split()

    if s[0] == 'push_front':
        stack.appendleft(s[1])

    elif s[0] == 'push_back':
        stack.append(s[1])

    elif s[0] == 'pop_front':
        if stack:
            print(stack.popleft())

        else:
            print(-1)

    elif s[0] == 'pop_back':
        if stack:
            print(stack.pop())

        else:
            print(-1)

    elif s[0] == 'size':
        print(len(stack))

    elif s[0] == 'empty':
        if stack:
            print(0)

        else:
            print(1)

    elif s[0] == 'front':
        if stack:
            print(stack[0])

        else:
            print(-1)


    elif s[0] == 'back':
        if stack:
            print(stack[-1])

        else:
            print(-1)

