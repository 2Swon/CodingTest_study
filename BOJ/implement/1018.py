N, M = map(int, input().split())

graph = []
result = []
for _ in range(N):
    graph.append(input())


for i in range(N-7):
    for j in range(M-7):
        draw_B = 0
        draw_W = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if graph[a][b] != 'W':
                        draw_B += 1

                    if graph[a][b] != 'B':
                        draw_W += 1

                else:
                    if graph[a][b] != 'B':
                        draw_B += 1

                    if graph[a][b] != 'W':
                        draw_W += 1

        result.append(draw_B)
        result.append(draw_W)

print(min(result))
