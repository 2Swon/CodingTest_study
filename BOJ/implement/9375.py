T = int(input())

for _ in range(T):
    N = int(input())
    wear_dict = {}
    for i in range(N):
        v, k = input().split()
        if wear_dict.get(k) == None:
            wear_dict[k] = set()
        wear_dict[k].add(v)
    result = 1
    for i in wear_dict.keys():
        result *= len(wear_dict[i])+1

    print(result-1)

