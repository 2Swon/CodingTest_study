N = int(input())

word_list = []

for _ in range(N):
    word_list.append(input())

word_list = set(word_list)

word_list = list(word_list)

word_list.sort()
word_list.sort(key=len)

for i in word_list:
    print(i)