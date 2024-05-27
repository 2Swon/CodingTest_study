N, M = map(int, input().split())
ans = []
def back(start):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(start, N+1):
        if i not in ans:
            ans.append(i)
            back(i+1)
            ans.pop(-1)

back(1)