N = int(input())
data = 1
cnt = 1

while N > data:
    data += 6 * cnt
    cnt += 1

print(cnt)