babbling = ["aya", "yee", "u", "maa"]
def solution(babbling):
    answer = 0

    for word in babbling:
        for pro in ["aya", "ye", "woo", "ma"]:
            if pro * 2 not in word:
                word=word.replace(pro,' ')
        if word.isspace():
            answer+=1

    return answer

print(solution(babbling))
