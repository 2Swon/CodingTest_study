import sys
input = sys.stdin.readline

N = int(input())

data = set()
for _ in range(N):
    command = list(map(str, input().split()))

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
        for i in range(1, 21):
            data.add(str(i))

    elif command[0] == 'empty':
        data.clear()

