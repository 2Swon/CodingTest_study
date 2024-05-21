def solution(citations):
    citations.sort(reverse=True)

    for idx, num in enumerate(citations):
        if idx >= num:
            return idx

    return len(citations)

print(solution([3, 0, 6, 1, 5]))

