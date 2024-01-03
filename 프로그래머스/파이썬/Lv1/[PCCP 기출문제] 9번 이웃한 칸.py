def solution(board, h, w):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    color = board[h][w]
    N = len(board)
    
    for d in range(4):
        nx = h + dx[d]
        ny = w + dy[d]

        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == color:
            answer += 1
            
    return answer