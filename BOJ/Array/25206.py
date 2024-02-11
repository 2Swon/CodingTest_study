score_list = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
              'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,
              'F': 0.0}

result = 0
total_score = 0
subject_list = []
for _ in range(20):
    name, score, grade = map(str, input().split())
    score = float(score)
    subject_list.append([name, score, grade])

for i in range(20):
    if subject_list[i][2] != 'P':
        result += subject_list[i][1] * score_list[subject_list[i][2]]
        total_score += subject_list[i][1]

print(result / total_score)
