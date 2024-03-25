N, M = map(int, input().split())

card_list = list(map(int, input().split()))

max_num = 0
sum_card = 0
for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_card = card_list[i] + card_list[j] + card_list[k]
            if sum_card <= M:
                max_num = max(sum_card, max_num)


print(max_num)