# def solution(h1, m1, s1, h2, m2, s2):
#     answer = 0
#     second = (h2-h1)*3600 + (m2-m1)*60 + s2-s1
#
#     for i in range(second):
#         s1 += 1
#         if s1 == 60:
#             s1 = 0
#             m1 += 1
#
#         if m1 == 60:
#             m1 = 0
#             h1 += 1
#
#         check_h = h1 + m1/12
#
#
#         if int(check_h) == s1 or m1 == s1:
#             if i == second-1:
#                 check_h
#             if int(check_h) == m1 == s1:
#                 answer += 1
#             else:
#                 answer += 1
#
#     return answer
#
# print(solution(0, 5, 30, 0, 7, 0))
