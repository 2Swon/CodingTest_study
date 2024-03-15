N = int(input())

switch_list = list(map(int,input().split()))

def switch(sex, number):
    if sex == 1:
        for i in range(1, N+1):
            if i % number == 0:
                switch_list[i-1] = 1 - switch_list[i-1]

    elif sex == 2:
        switch_list[number-1] = 1 - switch_list[number-1]
        i = 1
        while 0 <= number-1-i < N and 0 <= number-1+i < N and switch_list[number-1-i] == switch_list[number-1+i]:
            switch_list[number-1-i] = 1 - switch_list[number-1-i]
            switch_list[number-1+i] = 1 - switch_list[number-1+i]
            i += 1



M = int(input())
for _ in range(M):
    sex, number = map(int, input().split())
    switch(sex, number)

for i in range(N):
    print(switch_list[i], end=" ")
    if i % 20 == 19:
        print()
