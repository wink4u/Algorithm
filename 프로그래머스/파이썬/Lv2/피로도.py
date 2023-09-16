import itertools

def solution(k, dungeons):
    answer = 0
    dun_p = list(itertools.permutations(dungeons))
    
    for i in range(len(dun_p)):
        check_k = k
        cnt = 0
        for j in range(len(dun_p[i])):
            if dun_p[i][j][0] <= check_k:
                check_k -= dun_p[i][j][1]
                cnt += 1
                
        answer = max(answer, cnt)
        
    return answer