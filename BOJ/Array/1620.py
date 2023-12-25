from sys import stdin


def input():
    return stdin.readline().rstrip()

N, M = map(int, input().split())

id_dict = {}
name_dict = {}

for i in range(1, N+1):
    data = input()
    name_dict[i] = data
    id_dict[data] = i

for _ in range(M):
    data = input()
    if data.isdigit():
        print(name_dict[int(data)])

    else:
        print(id_dict[data])