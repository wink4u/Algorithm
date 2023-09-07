def solution(n, s):
    
    avg = s // n
    if avg == 0:
        return [-1]
    
    
    cnt = 0
    answer = []
    while cnt != n:
        cnt += 1
        answer.append(avg)
    
    total = avg * cnt
    
    if s - total:
        for i in range(s - total):
            answer[i] += 1
    
    answer.sort()
    
    
    return answer