from sys import stdin

input = stdin.readline


def solution():
    T = int(input())
    for _ in range(T):
        answer = 100
        N = int(input())
        arr = list(input().split())
        if N > 32:
            print(0)
            continue

        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):

                    AB = 0
                    BC = 0
                    AC = 0

                    if arr[i] != arr[j]:
                        for l in range(4):
                            if arr[i][l] != arr[j][l]:
                                AB += 1
                    if arr[j] != arr[k]:
                        for l in range(4):
                            if arr[j][l] != arr[k][l]:
                                BC += 1

                    if arr[i] != arr[k]:
                        for l in range(4):
                            if arr[i][l] != arr[k][l]:
                                AC += 1

                    answer = min(answer, AB + BC + AC)

        print(answer)


solution()