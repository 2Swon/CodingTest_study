T = int(input())

for j in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    max_future_price = 0
    total_profit = 0

    for i in reversed(range(N)):
        if prices[i] > max_future_price:
            max_future_price = prices[i]
        total_profit += max_future_price - prices[i]

    print(f'#{j} {total_profit}')