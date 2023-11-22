from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    
    history = defaultdict(int);

    for i in range(len(name)):
        history[name[i]] = yearning[i]
    
    for i in range(len(photo)):
        
        res = 0
        for j in range(len(photo[i])):
            
            res += history[photo[i][j]]
        
        answer.append(res)
    
    return answer

