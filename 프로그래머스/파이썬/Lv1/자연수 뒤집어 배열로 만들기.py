def solution(n):
    answer = []
    
    if n < 10:
        answer.append(n)
        return answer
    
    while True:
        answer.append(n % 10)
        
        n = n // 10
        
        if n < 10:
            answer.append(n)
            break
    
    return answer