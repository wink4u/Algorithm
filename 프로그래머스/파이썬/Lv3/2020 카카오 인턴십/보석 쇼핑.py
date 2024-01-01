from collections import defaultdict

def solution(gems):
    answer = [0, len(gems)]
    
    start, end = 0, 0
    
    gem_cnt = len(set(gems))
    gem_dict = {gems[0] : 1}

    while start < len(gems) and end < len(gems):
        
        if len(gem_dict) == gem_cnt:
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
            