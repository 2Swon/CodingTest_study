N = int(input())

for _ in range(N):
    data = input()
    result = []
    for i in data:
        if i == '(':
            result.append('(')

        else:
            if result:
                result.pop(-1)
            else:
                print("NO")
                break


    else:
        if result:
            print('NO')

        else:
            print('YES')

