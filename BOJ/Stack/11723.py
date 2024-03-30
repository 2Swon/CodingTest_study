import sys
input = sys.stdin.readline

N = int(input())

data = set()
for _ in range(N):
    command = list(map(str, input().split()))
    if len(command) == 2:
        command[1] = int(command[1])
    if command[0] == 'add':
        data.add(command[1])

    elif command[0] == 'check':
        if command[1] in data:
            print(1)

        else:
            print(0)

    elif command[0] == 'remove':
        if command[1] in data:
            data.remove(command[1])


    elif command[0] == 'toggle':
        if command[1] in data:
            data.remove(command[1])

        else:
            data.add(command[1])

    elif command[0] == 'all':
        data = set()
        data.update((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))

    elif command[0] == 'empty':
        data.clear()

