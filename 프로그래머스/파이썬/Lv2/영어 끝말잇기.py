def solution(n, words):
    

    total = 0
    check_v = [words[0]]
    
    cnt = 1
    for i in range(1, len(words)):
        if cnt == n:
            cnt = 0
            
        if words[i] in check_v or check_v[-1][-1] != words[i][0]:
            return [cnt + 1, i // n + 1]
        else:
            check_v.append(words[i])
            cnt += 1
            
    return [0, 0]