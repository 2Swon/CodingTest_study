form = list(input().split('-'))
res_list = []
for i in form:
    sum = 0
    temp = i.split('+')
    for j in temp:
        sum += int(j)

    res_list.append(sum)
result = res_list[0]
for i in range(1, len(res_list)):
    result -= res_list[i]

print(result)