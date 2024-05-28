N, M = map(int, input().split())

ans = []
def back(start):
    if len(ans) == M:
        print(*ans)
        return

    else:
        for i in range(start, N+1):
            ans.append(i)
            if ans[-1] == i:
                back(i)
                ans.pop(-1)
            else:
                back(i+1)
                ans.pop(-1)


back(1)