N, K = map(int, input().split())

def fac(n):
    if n == 0:
        return 1

    else:
        return n * fac((n-1))

print(fac(N)// (fac(K)*fac(N-K)))