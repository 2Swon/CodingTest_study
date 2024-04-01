N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

result = 0

for i in coins:
    result += K // i
    K %= i

print(result)