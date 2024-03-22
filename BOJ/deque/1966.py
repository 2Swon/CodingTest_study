t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = 1

    while data:
        if data[0] < max(data):
            data.append(data.pop(0))

        else:
            if m == 0:
                break

            data.pop(0)
            result += 1

        m = m-1 if m > 0 else len(data)-1

    print(result)