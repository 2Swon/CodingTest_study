T = int(input())

for _ in range(T):
    DP = [0] * 13
    N = int(input())
    DP[1] = 1
    DP[2] = 2
    DP[3] = 4

    for i in range(4, N+1):
        DP[i] = DP[i-3] + DP[i-2] + DP[i-1]

    print(DP[N])


