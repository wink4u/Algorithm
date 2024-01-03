def solution(data, ext, val_ext, sort_by):
    answer = []
    # ext 값이 val_ext 보다 작은 데이터값
    # sort_by 기준
    N = 0
    S = 0
    if ext == 'date':
        N = 1
    elif ext == 'maximum':
        N = 2
    elif ext == 'remain':
        N = 3
    
    if sort_by == 'date':
        S = 1
    elif sort_by == 'maximum':
        S = 2
    elif sort_by == 'remain':
        S = 3
        
    for i in range(len(data)):
        if data[i][N] < val_ext:
            answer.append(data[i])

    answer.sort(key = lambda x : x[S])

    return answer