N, M = map(int, input().split())
N_list = list(map(int, input().split()))

N_list.sort()
ans = []
def back():
    if len(ans) == M:
        print(*ans)
        return

    else:
        for i in range(0, len(N_list)):
            if N_list[i] not in ans:
                ans.append(N_list[i])
                back()
                ans.pop(-1)

back()