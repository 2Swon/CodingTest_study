N = int(input())

DP = [0]*1000001

for i in range(2, N+1):
    DP[i] = DP[i-1] + 1

    if i % 2 == 0:
        DP[i] = min(DP[i//2]+1, DP[i])

    if i % 3 == 0:
        DP[i] = min(DP[i//3]+1, DP[i])


print(DP[N])