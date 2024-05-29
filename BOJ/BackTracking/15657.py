N, M = map(int, input().split())
N_list = list(map(int, input().split()))

N_list.sort()
ans = []
def back(start):
    if len(ans) == M:
        print(*ans)
        return

    else:
        for i in range(start, len(N_list)):
            ans.append(N_list[i])
            if N_list[i] not in ans:
                back(i+1)
                ans.pop(-1)

            else:
                back(i)
                ans.pop(-1)

back(0)