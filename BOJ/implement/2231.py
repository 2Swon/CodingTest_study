N = int(input())

check = False
for i in range(1, N):
    tmp = i
    num = tmp
    while tmp > 0:
        a = tmp % 10
        tmp //= 10
        num += a

    if num == N:
        check = True
        print(i)
        break

if check == False:
    print(0)
