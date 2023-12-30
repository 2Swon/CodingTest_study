from collections import deque

n = int(input())

q = deque(enumerate(map(int, input().split())))

ans = []

while q:
    idx, number = q.popleft()
    ans.append(idx + 1)

    if number > 0:
        q.rotate(-(number-1))

    elif number < 0:
        q.rotate(-number)

print(*ans)