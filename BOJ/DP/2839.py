import math
N = int(input())

DP = [0]*5001
DP[0] = math.inf
DP[1] = math.inf
DP[2] = math.inf
DP[3] = 1
DP[4] = math.inf
DP[5] = 1
for i in range(6, 5001):
    DP[i] = min(DP[i-3]+1, DP[i-5]+1)

if DP[N] == math.inf:
    print(-1)

else:
    print(DP[N])
