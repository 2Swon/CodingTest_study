T = int(input())

for _ in range(T):
    DP = [0] * 101
    N = int(input())
    DP[1] = 1
    DP[2] = 1
    DP[3] = 1

    for i in range(4, N+1):
        DP[i] = DP[i-2] + DP[i-3]

    print(DP[N])