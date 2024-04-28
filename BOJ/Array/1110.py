N = int(input())

cnt = 0
num = N

while True:
    if num < 10:
        a = 0

    else:
        a = num // 10

    b = num % 10

    temp = a + b

    num = b*10 + temp%10

    cnt += 1

    if num == N:
        break


print(cnt)


