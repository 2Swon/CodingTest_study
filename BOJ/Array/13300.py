import math
N, K = map(int, input().split())
student_list = [[0 for _ in range(2)] for _ in range(6)]
result = 0
for _ in range(N):
    sex, grade = map(int, input().split())

    student_list[grade-1][sex] += 1

for i in range(len(student_list)):
    for j in range(len(student_list[i])):
        if 0 < student_list[i][j] <= K:
            result += 1
        else:
            result += math.ceil(student_list[i][j]/K)


print(result)



