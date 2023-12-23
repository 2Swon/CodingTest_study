N = int(input())

time = []

for _ in range(N):
    s, e = map(int, input().split())
    time.append([s, e])

time.sort(key=lambda x: (x[1], x[0]))

endpoint = 0
cnt = 0
for start, end in time:
    if endpoint <= start:
        endpoint = end
        cnt += 1

print(cnt)