T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    k = x
    found = False

    while k <= M * N:
        if (k - x) % M == 0 and (k - y) % N == 0:
            print(k)
            found = True
            break

        k += M

    if not found:
        print(-1)