N = int(input())

stair_list = [0] * 301

for i in range(1, N+1):
    stair_list[i] = int(input())


DP = [0] * 301
DP[1] = stair_list[1]
DP[2] = stair_list[1] + stair_list[2]
DP[3] = max(stair_list[3]+stair_list[2], stair_list[3] + stair_list[1])

for i in range(4, N+1):
    DP[i] = max(DP[i-3] + stair_list[i] + stair_list[i-1], DP[i-2] + stair_list[i])

print(DP[N])