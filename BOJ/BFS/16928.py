from collections import deque

def bfs():
    queue = deque([1])
    visited[1] = True
    while queue:
        now = queue.popleft()
        for move in range(1,7):
            check_move = now+move
            if 0 < check_move <= 100 and not visited[check_move]:
                if check_move in ladder.keys():
                    check_move = ladder[check_move]

                if check_move in snack.keys():
                    check_move = snack[check_move]

                if not visited[check_move]:
                    queue.append(check_move)
                    visited[check_move] = True
                    board_cnt[check_move] = board_cnt[now] + 1



if __name__ == '__main__':
    N, M = map(int,input().split())
    board_cnt = [0] * 101
    visited = [False] * 101

    snack = dict()
    ladder = dict()
    for _ in range(N):
        i,j = map(int,input().split())
        ladder[i] = j
    for _ in range(M):
        i,j = map(int,input().split())
        snack[i] = j

    bfs()
    print(board_cnt[100])