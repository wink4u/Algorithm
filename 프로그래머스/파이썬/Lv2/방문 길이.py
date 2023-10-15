def solution(dirs):   
    # 상 하 좌 우
    sx, sy = 0, 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    check = []
    
    for command in dirs:
        temp = []
        temp.append((sx, sy))
        if command == 'U':
            nx = sx + dx[0]
            ny = sy + dy[0]
        elif command == 'D':
            nx = sx + dx[1]
            ny = sy + dy[1]
        elif command == 'L':
            nx = sx + dx[2]
            ny = sy + dy[2]
        else:
            nx = sx + dx[3]
            ny = sy + dy[3]
    
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            sx = nx
            sy = ny
            temp.append((sx, sy))
            temp.sort()
            
            if temp not in check:
                check.append(temp)
    
    return len(check)