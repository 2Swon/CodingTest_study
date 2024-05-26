def solution(phone_book):
    book_set = set(phone_book)
    for num in book_set:
        for i in range(1, len(num)):
            length = num[:i]
            if length in book_set:
                return False

    return True

print(solution(["119", "97674223", "1195524421"]))