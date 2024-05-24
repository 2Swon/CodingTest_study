import sys
N = int(input())
arr = []
for _ in range(N):
    S, T = map(str, sys.stdin.readline().split())

    for i, v in enumerate(S):
        if v == 'x' or v == 'X':
            idx = i

    ans = T[idx].upper()


    arr.append(ans)

for i in arr:
    print(i, end="")