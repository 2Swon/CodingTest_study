def solution(board, h, w):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    answer = 0
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        if 0 <= nx < len(board) and 0 <= ny < len(board):
            if board[h][w] == board[nx][ny]:
                answer += 1

    return answer