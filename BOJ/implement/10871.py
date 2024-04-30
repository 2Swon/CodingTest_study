n, x = map(int, input().split())

data = list(map(int, input().split()))

for i in data:
    if x > i:
        print(i)