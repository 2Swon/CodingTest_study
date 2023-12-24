N = int(input())

DP = [0 for _ in range(N+1)]

num_list = [i*i for i in range(1, 224)]
for i in range(1, N+1):
    if i in num_list:
        DP[i] = 1

    else:
        for j in num_list:
            if i-j > 0:
                DP[i] = min(DP[i], DP[i-j])+1

print(DP[N])
