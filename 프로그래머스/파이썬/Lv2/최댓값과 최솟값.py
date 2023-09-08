def solution(s):
    answer = ''
    
    s_list = s.split()
    
    max_v = int(s_list[0])
    min_v = int(s_list[0])
    for i in range(1, len(s_list)):
        max_v = max(max_v, int(s_list[i]))
        min_v = min(min_v, int(s_list[i]))
    
    answer = str(min_v) + ' ' + str(max_v)
    return answer