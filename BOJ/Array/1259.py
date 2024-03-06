word_list = []
while True:
    word = input()
    if word == '0':
        break
    word_list.append(list(word))

temp = []
for i in word_list:
    temp.append(list(reversed(i)))

for i in range(len(word_list)):
    if word_list[i] != temp[i]:
        print('no')

    else:
        print('yes')



