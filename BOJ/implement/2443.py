n = int(input())

for i in range(n):
    for j in range(n-i, n):
        print(" ", end="")

    for k in range(2*n-1, 2*i, -1):
        print("*", end="")

    print()

















