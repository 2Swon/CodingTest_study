import sys
input = sys.stdin.readline

N, T = map(int, input().split())

arr = list(map(int, input().split()))
S = [0] * 100001
S[0] = arr[0]
S[1] = arr[1] + S[0]
for i in range(1, len(arr)):
    S[i] = arr[i] + S[i-1]

for _ in range(T):
    i, j = map(int, input().split())
    print(S[j-1]-S[i-1]+arr[i-1])


