def solution(bandage, health, attacks):
    answer = health
    time = attacks[-1][0]
    max_health = health
    attacks_dict = {}
    count = 0
    for i in attacks:
        attacks_dict[i[0]] = i[1]

    now = 0

    while now <= time:
        if now not in attacks_dict:
            count += 1
            if count % bandage[0] != 0:
                answer += bandage[1]
                if answer > max_health:
                    answer = max_health
            else:
                answer += bandage[2]
                if answer > max_health:
                    answer = max_health

        else:
            answer -= attacks_dict[now]
            count = 0
            if answer <= 0:
                return -1
        now += 1

    return answer


bandage = [5, 1, 5]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
print(solution(bandage, health, attacks))
