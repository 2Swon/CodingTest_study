N, M = map(int, input().split())
ans = []
def back():
    if len(ans) ==  M:
        print(*ans)
        return

    for i in range(1, N+1):
        if i not in ans:
            ans.append(i)
            back()
            ans.pop(-1)

back()