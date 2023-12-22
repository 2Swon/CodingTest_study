import sys
input = sys.stdin.readline

N, M = map(int, input().split())

wood_list = list(map(int, input().split()))

start = 1
end = max(wood_list)

while start <= end:
    mid = (start + end) // 2
    meters = 0
    for i in wood_list:
        if mid < i:
            meters += (i - mid)

    if meters < M:
        end = mid - 1

    else:
        start = mid + 1

print(end)

