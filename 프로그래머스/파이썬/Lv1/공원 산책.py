def solution(park, routes): 
    n = len(park)
    m = len(park[0])
    
    sx, sy = 0, 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    move_d = {'N' : 0, 'S' : 1, 'W' : 2, 'E' : 3}
    
    for i in range(len(park)):
        flag = 0
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                sx, sy = i, j
                flag = 1
                break
        
        if flag == 1:
            break
    
    for i in range(len(routes)):
        move = routes[i].split()
        
        time = int(move[1])
        
        temp_x, temp_y = sx, sy
        for j in range(time):
            nx = sx + dx[move_d[move[0]]]
            ny = sy + dy[move_d[move[0]]]
            
            if 0 <= nx < n and 0 <= ny < m and park[nx][ny] != 'X':
                sx = nx
                sy = ny
            else:
                sx = temp_x
                sy = temp_y
                break
    
    return [sx, sy]