# n = int(input())
# stack, res, find = [], [], True
#
# now = 1
# for _ in range(n):
#     num = int(input())
#
#     while now <= num:
#         stack.append(now)
#         res.append('+')
#         now += 1
#
#     if stack[-1] == num:
#         stack.pop()
#         res.append('-')
#
#     else:
#         find = False
#
# if find:
#     for i in res:
#         print(i)
# else:
#     print("NO")

N = int(input())

stack, result, check = [], [], True
num = 1
for _ in range(N):

    number = int(input())

    while num <= number:
        stack.append(num)
        result.append('+')
        num += 1

    if stack[-1] == number:
        stack.pop()
        result.append('-')

    else:
        check = False

if check:
    for i in result:
        print(i)

else:
    print('NO')





















