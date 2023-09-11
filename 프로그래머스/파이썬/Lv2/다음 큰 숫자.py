def solution(n):
    answer = 0
    
    n_bin = bin(n)[2:]
    one_cnt = n_bin.count('1')
    
    while True:
        n += 1
        temp_bin = bin(n)[2:]
        if temp_bin.count('1') == one_cnt:
            answer = n
            break
            
    return answer