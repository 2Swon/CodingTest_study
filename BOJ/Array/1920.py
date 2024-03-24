N = int(input())
num_list = set(map(int, input().split()))
M = int(input())
find_list = list(map(int, input().split()))

for i in find_list:
    print('1') if i in num_list else print('0')