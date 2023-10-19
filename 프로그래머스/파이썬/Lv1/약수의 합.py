def solution(n):
    cnt = 1
    answer = 0
    while cnt != n + 1:
        if n % cnt == 0:
            answer += cnt
        
        cnt += 1
            
    return answer