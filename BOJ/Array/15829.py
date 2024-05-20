N = int(input())

arr = list(input())
idx = 0
ans = 0
for i in arr:
    num = ord(i) - 96
    ans += num * 31 ** idx
    idx += 1

print(ans)
