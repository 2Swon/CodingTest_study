N = int(input())
a = range(1, N+1)
S = 0
for i in range(0, N):
    S += a[i]

print(S)
print(type(a))