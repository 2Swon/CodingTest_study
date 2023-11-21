# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#
# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
#
# 예제 입력 1
# 5
# 예제 출력 1
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
n = int(input())

for i in range(n):
    for j in range(n-i, n):
        print(" ", end="")

    for k in range(2*n-1, 2*i, -1):
        print("*", end="")

    print()

for i in range(1, n):
    for j in range(n-i, 1, -1):
        print(" ", end="")

    for k in range(2*i+1):
        print("*", end="")

    print()