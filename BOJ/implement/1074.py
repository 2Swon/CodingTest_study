N, r, c = map(int, input().split())
N = 2**N
num = 0
def solution(x, y, n):
    global num

    if x > r or y > c or x+n <= r or y+n <= c:
        num += n**2
        return

    if n == 2:
        for i in range(x, x+n):
            for j in range(y, y+n):
                if i == r and j == c:
                    print(num)
                num += 1

    else:
        solution(x, y, n//2)
        solution(x, y + n//2, n//2)
        solution(x + n//2, y, n//2)
        solution(x + n//2, y + n//2, n//2)

solution(0, 0, N)
