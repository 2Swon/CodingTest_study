N = int(input())
M = int(input())
arr = input()

cnt, cursor, result = 0, 0, 0

while cursor < M-1:

    if arr[cursor:cursor+3] == 'IOI':
        cursor += 2
        cnt += 1

        if cnt == N:
            result += 1
            cnt -= 1

    else:
        cnt = 0
        cursor += 1


print(result)


