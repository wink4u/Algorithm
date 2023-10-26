def solution(record):
    answer = []
    
    name = {}
    
    temp = []
    for log in record:
        log_content = log.split()
        
        if log_content[0] == 'Enter' or log_content[0] == 'Change':
            name[log_content[1]] = log_content[2]
        
        if log_content[0] == 'Enter':
            temp.append([log_content[1], 0])
        elif log_content[0] == 'Leave':
            temp.append([log_content[1], 1])
    
    
    for result in temp:
        if result[1] == 0:
            answer.append(f'{name[result[0]]}님이 들어왔습니다.')
        else:
            answer.append(f'{name[result[0]]}님이 나갔습니다.')
    return answer