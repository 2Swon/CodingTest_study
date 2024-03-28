N, K = map(int, input().split())

que = []
result = []
for i in range(1, N+1):
    que.append(i)
idx = 0
while que:
    idx += K-1

    if idx >= len(que):
        idx %= len(que)

    result.append(str(que.pop(idx)))

print("<", ", ".join(result), ">", sep="")

