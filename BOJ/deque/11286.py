import heapq
import sys
input = sys.stdin.readline
N = int(input())

data = []
for _ in range(N):
    command = int(input())

    if command == 0:
        if data:
            print(heapq.heappop(data)[1])

        else:
            print(0)
    else:
        heapq.heappush(data, (abs(command), command))

