from collections import deque
x , y= map(int,input().split())

array = [-1]*10001
def bfs(x):
    que = deque()
    que.append(x)
    while que:
        v = que.popleft()
        for node in [v+1, v-1, v*2]:
            if node < 0 or node > 10000:
                continue
            if array[node] == -1:
                array[node] = array[v] + 1
                que.append(node)

array[x] = 0
bfs(x)
print(array[y])

