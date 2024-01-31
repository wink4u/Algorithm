import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
roads = []
rain = []

for i in range(R):
    temp = list(input().strip())
    for j in range(len(temp)):
        if temp[j] == 'W':
            W = [i, j]
        if temp[j] == '*':
            rain.append([i, j])
    roads.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move_person(rain):
    q = deque()
    q.append(W)
    visit = [[-1 for _ in range(C)] for _ in range(R)]
    visit[W[0]][W[1]] = 0
    
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            if roads[x][y] == '*':
                continue
                
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if 0 <= nx < R and 0 <= ny < C and visit[nx][ny] == -1:
                    if roads[nx][ny] == '.':
                        q.append((nx, ny))
                        visit[nx][ny] = visit[x][y] + 1
                    elif roads[nx][ny] == 'H':
                        return visit[x][y] + 1
                        
        rain = move_rain(rain)
        
    return 'FAIL'
    
def move_rain(rain):
    tmp = []
    for i in range(len(rain)):
        x, y = rain[i][0], rain[i][1]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < R and 0 <= ny < C:
                if roads[nx][ny] == '.':
                    roads[nx][ny] = '*'
                    tmp.append((nx,ny))

    return tmp
    
res = move_person(rain)
print(res)