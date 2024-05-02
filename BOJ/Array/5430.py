from collections import deque


T = int(input())


for i in range(T):
    is_error = False
    command_list = list(input())

    N = int(input())

    data = input()
    if N == 0:
        que = deque()

    else:
        numbers_string = data[1:-1]
        que = deque(numbers_string.split(','))


    R = 0

    for j in command_list:
        if j == 'R':
            R += 1
        elif j == 'D':
            if not que:
                is_error = True
                print('error')
                break

            else:
                if R % 2 == 0:
                    que.popleft()

                else:
                    que.pop()

    if not is_error:
        if R % 2 == 0:
            print('[' + ",".join(que) + ']')

        else:
            que.reverse()
            print('[' + ",".join(que) + ']')




