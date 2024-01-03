from collections import defaultdict

def solution(bandage, health, attacks):
    answer = health
    # bandage 시전 시간, 초당 회복량, 추가 회복량
    
    pre_time = 0
    for time, dmg in attacks:
        # 현재시간, 이전시간 사이의 회복 타임
        cnt = time - pre_time - 1
        # 이전시간을 현재시간으로 할당
        pre_time = time
        
        # 시전시간 카운트
        health_cnt = 0
        while cnt:
            health_cnt += 1
            
            # 시전시간에 만족되는 값이면
            if health_cnt == bandage[0]:
                # 추가회복 및 초기화
                answer += bandage[2]
                health_cnt = 0
            
            # 원래 회복량
            answer += bandage[1]
            cnt -= 1
        
        # 최대체력 보다 높다면 최대체력으로
        if answer >= health:
            answer = health
        
        # 데미지를 주고
        answer -= dmg
        # 만약 0이하면 -1로 할당후 break
        if answer <= 0:
            answer = -1
            break
                
    return answer
