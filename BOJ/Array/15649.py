N, M = map(int, input().split())

visited = [False] * N

array = []

for i in range(N):
    array.append(i+1)


ans = []
def solution():
    check = 0 
    if len(ans) == M:
        print(*ans)
        return
    
    else:
        for i in range(N):
            if check != array[i] and not visited[i]:
                ans.append(array[i])
                visited[i] = True
                check = array[i]

                solution()

                ans.pop()
                visited[i] = False

solution()