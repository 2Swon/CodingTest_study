N = int(input())

num_list = list(map(int, input().split()))

def is_prime_num(n):
    if n == 1:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False

    else:
        return True

cnt = 0

for i in num_list:
    if is_prime_num(i):
        cnt += 1

print(cnt)

