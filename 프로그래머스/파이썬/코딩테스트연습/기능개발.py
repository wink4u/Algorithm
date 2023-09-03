def solution(progresses, speeds):
    res = []
    answer = []
    
    # progresses에 있는 단계를 while문으로 판단
    for i in range(len(progresses)):
        cnt = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            cnt += 1
            
        res.append(cnt)
    
    # prev 값과 지금값이 비교하면서 rcnt를 올리고
    # 판단함
    rcnt = 1
    prev = res[0]
    for i in range(1, len(res)):
        if res[i] > prev:
            answer.append(rcnt)
            prev = res[i]
            rcnt = 1
        else:
            rcnt += 1
            
    answer.append(rcnt)
    
    return answer
