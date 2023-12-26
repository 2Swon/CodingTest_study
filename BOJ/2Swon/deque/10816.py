# n = int(input())
# card_list = sorted(list(map(int, input().split())))
# m = int(input())
# find_list = list(map(int, input().split()))
#
# def binaray_search(N, card_list, start, end):
#     if start > end:
#         return 0
#
#     mid = (start+end)//2
#
#     if N == card_list[mid]:
#         return card_list[start:end+1].count(N)
#     elif N > card_list[mid]:
#         return binaray_search(N, card_list, mid+1, end)
#
#     elif N < card_list[mid]:
#         return binaray_search(N, card_list, start, mid-1)

import sys
input = sys.stdin.readline
n = int(input())
card_list = list(map(int,input().split()))
m = int(input())
find_list = list(map(int,input().split()))

ans = [0 for _ in range(m)]

for num in card_list:
    if num in find_list:
        ans[find_list.index(num)] += 1

print(*ans)

