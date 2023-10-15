def solution(skill, skill_trees):
    answer = 0
    
    skills = list(skill)
    
    for tree in skill_trees:
        cnt = 0
        flag = 0
        
        for i in tree:
            if i in skills:
                if i == skills[cnt]:
                    cnt += 1
                else:
                    flag = 1
                    break
        
        if flag == 0:
            answer += 1
        
    return answer