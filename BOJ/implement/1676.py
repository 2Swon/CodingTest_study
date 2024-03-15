N = int(input())

cnt = 0

while N>1:
    cnt += N//5
    N = N //5

print(cnt)
