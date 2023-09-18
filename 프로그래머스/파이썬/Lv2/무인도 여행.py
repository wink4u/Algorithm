from collections import deque

answer = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, x, y):
    global visited
    q = deque()    
    q.append((x, y))
    visited[x][y] = 1
    
    result = 0
    result +=int(maps[x][y]) 
    while q:
        x, y = q.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                result += int(maps[nx][ny])
                
    answer.append(result)
    
def solution(maps):
    global visited
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            
            if maps[i][j] != 'X' and not visited[i][j]:
                bfs(maps, i, j)
    
    if answer:
        return sorted(answer)
    else:
        return [-1]