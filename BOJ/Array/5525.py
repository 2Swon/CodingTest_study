# N = int(input())
# M = int(input())
# arr = input()
#
# check = 'IO' * N + 'I'
# cnt = 0
# for i in range(M - len(check)+1):
#     if check == arr[i:i+len(check)]:
#         cnt += 1
#
# print(cnt)

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


