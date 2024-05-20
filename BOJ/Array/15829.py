N = int(input())

M = 1234567891
r = 31
arr = input()
ans = 0
for i in range(N):
    num = ord(arr[i]) - 96
    ans += num * r ** i

print(ans % M)
