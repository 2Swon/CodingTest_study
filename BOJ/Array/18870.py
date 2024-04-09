N = int(input())

arr = list(map(int, input().split()))

arr_sorted = sorted(list(set(arr)))
res = {}
for i in range(len(arr_sorted)):
    res[arr_sorted[i]] = i

for i in arr:
    print(res[i], end=" ")