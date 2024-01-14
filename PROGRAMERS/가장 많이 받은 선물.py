import numpy as np
def solution(friends, gifts):
    answer = [0] * len(friends)
    gift_table = [[0 for _ in range(len(friends))] for _ in range(len(friends))]

    for gift in gifts:
        g, r = gift.split()
        gift_table[friends.index(g)][friends.index(r)] += 1

    array = np.array(gift_table)

    given = array.sum(axis=1)
    recieve = array.sum(axis=0)
    total = list(given - recieve)

    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if gift_table[i][j] > gift_table[j][i]:
                answer[i] += 1
            elif gift_table[j][i] > gift_table[i][j]:
                answer[j] += 1

            else:
                if total[i] > total[j]:
                    answer[j] += 1

                if total[j] > total[i]:
                    answer[i] += 1

    return max(answer)

