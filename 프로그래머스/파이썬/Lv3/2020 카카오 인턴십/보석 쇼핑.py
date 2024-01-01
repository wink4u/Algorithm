from collections import defaultdict

def solution(gems):
    answer = [0, len(gems)]
    # 투포인터인데 start, end를 0기준으로 시작
    start, end = 0, 0
    # 보석의 개수
    gem_cnt = len(set(gems))
    gem_dict = {gems[0] : 1}
    # start, end가 gems의 개수보다 적을때 while문
    while start < len(gems) and end < len(gems):
        # 보석을 다 찾았다면
        if len(gem_dict) == gem_cnt:
            # start, end와 answer 기준과 비교
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            else:
                gem_dict[gems[start]] -= 1
                if gem_dict[gems[start]] == 0:
                    del gem_dict[gems[start]]
                start += 1
        else:
            end += 1
            if end == len(gems):
                break
            
            gem_dict[gems[end]] = gem_dict.get(gems[end], 0) + 1
    
    print(answer)
    return [answer[0] + 1, answer[1] + 1]
            