N = int(input())

for i in range(N):
    for j in range(i + 1, N):
        print(" ", end="")

    for k in range(i+1):
        print("*", end="")

    print()