a, b = map(int, input().split())

def gcd(x, y):
    while y > 0:
        x, y = y, x % y

    return x

print(gcd(a, b))
print(int(a*b/gcd(a, b)))
