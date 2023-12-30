import sys

input = sys.stdin.readline

_ = input()
N = sorted(map(int, input().split()))
_ = input()
M = map(int, input().split())

def binary_search(array, target, start, end):

    if start > end:
        return 0

    mid = (start + end) // 2

    if array[mid] == target:
        return array[start:end+1].count(target)

    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary_search(N, n, start, end)

result = []
for x in M:
    if x in n_dic:
        result.append(str(n_dic[x]))
    else:
        result.append('0')

output = ' '.join(result)
print(output)