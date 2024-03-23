n = int(input())
stack, res, find = [], [], True

now = 1
for _ in range(n):
    num = int(input())

    while now <= num:
        stack.append(now)
        res.append('+')
        now += 1

    if stack[-1] == num:
        stack.pop()
        res.append('-')

    else:
        find = False

if find:
    for i in res:
        print(i)
else:
    print("NO")