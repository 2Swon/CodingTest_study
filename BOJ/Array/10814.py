N = int(input())

data = []

for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    data.append((age, name))

data.sort(key= lambda x:x[0])

for i in data:
    print(*i)