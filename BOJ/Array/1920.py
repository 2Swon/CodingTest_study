# N = int(input())
# num_list = set(map(int, input().split()))
# M = int(input())
# find_list = list(map(int, input().split()))
#
# for i in find_list:
#     print('1') if i in num_list else print('0')

N = int(input())

num_list = list(map(int, input().split()))

M = int(input())

find_list = list(map(int, input().split()))

num_list.sort()

for i in find_list:
    start = 0
    end = len(num_list)-1

    while start <= end:
        mid = (start + end) // 2

        if num_list[mid] == i:
            print(1)
            break

        elif num_list[mid] > i:
            end = mid - 1

        else:
            start = mid + 1

    if num_list[mid] != i:
        print(0)