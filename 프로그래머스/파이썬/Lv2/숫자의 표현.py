def solution(n):
    answer = 1
    
    # 등차수열 합공식
    # n { 2a + (n - 1)} / 2
    
    a = 1
    while a != n:
        k = 1
        while True:
            result = (k * (2 * a + (k - 1))) / 2
            if result > n:
                break
            
            if result == n:
                answer += 1
            
            k += 1
            
        a += 1
        
    return answer