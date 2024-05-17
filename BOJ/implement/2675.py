T = int(input())

for _ in range(T):
    n, word = map(str, input().split())
    N = int(n)

    for i in word:
        for j in range(N):
            print(i, end="")

    print()