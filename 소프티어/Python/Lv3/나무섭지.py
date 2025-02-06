import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
ghost = []
visit_g = [[0 for _ in range(m)] for _ in range(n)]
visit_h = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    tmp = list(input())
    for j in range(len(tmp)):
        if tmp[j] == 'N':
            sx, sy = i, j
        elif tmp[j] == 'G':
            ghost.append([i, j])
            visit_h[i][j] = 1
    board.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_g(ghosts):
    tmp = []
    while ghosts:
        gx, gy = ghosts.pop()
        for d in range(4):
            gnx = gx + dx[d]
            gny = gy + dy[d]
            if 0 <= gnx < n and 0 <= gny < m and not visit_g[gnx][gny]:
                visit_g[gnx][gny] = 1
                tmp.append((gnx, gny))

    return tmp
    
def bfs_h(sx, sy, ghosts):
    q = deque()
    q.append((sx, sy))
    visit_h[sx][sy] = 1

    while q:

        for _ in range(len(q)):
            x, y = q.popleft()

            if board[x][y] == 'D':
                return 'Yes'

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != '#' and not visit_h[nx][ny]:
                    if not visit_g[nx][ny]:
                        visit_h[nx][ny] = 1
                        q.append((nx, ny))

        ghosts = bfs_g(ghosts)
            
    return 'No'

print(bfs_h(sx,sy, ghost))