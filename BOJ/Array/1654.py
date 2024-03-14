N, K = map(int, input().split())

lines = []

for _ in range(N):
    lines.append(int(input()))

start = 1
end = max(lines)

while start <= end:
    line = 0
    mid = (start+end) //2

    for i in lines:
        line += i // mid

    if line >= K:
        start = mid + 1

    else:
        end = mid - 1

print(end)