N, M = map(int, input().split())

data_dict = {}
result_list = []
for _ in range(N):
    url, password = map(str, input().split())
    data_dict.update({url:password})

for _ in range(M):
    url = input()
    result_list.append(data_dict[url])

for i in result_list:
    print(i)
