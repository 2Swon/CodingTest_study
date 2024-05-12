T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    DP = [x for x in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            DP[j] += DP[j-1]

    print(DP[-1])
