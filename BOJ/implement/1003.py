N = int(input())

for _ in range(N):
    M = int(input())
    a, b = 1, 0

    for i in range(M):
        a, b = b, a+b

    print(a, b)
