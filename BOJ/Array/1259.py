word_list = []
while True:
    word = input()
    if word == '0':
        break
    word_list.append(list(word))


for i in word_list:
    if i != i[::-1]:
        print('no')

    else:
        print('yes')



