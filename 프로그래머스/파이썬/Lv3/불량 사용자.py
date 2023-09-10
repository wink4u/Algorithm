from itertools import permutations

def find_ban(combi, check_ban):
    for i in range(len(combi)):
        if len(combi[i]) != len(check_ban[i]):
                return False
        
        for j in range(len(combi[i])):
            if combi[i][j] != check_ban[i][j]:
                if check_ban[i][j] != '*':
                    return False
                else:
                    continue
                
    return True
                
    
    
def solution(user_id, banned_id):
    permu = list(permutations(user_id, len(banned_id)))

    find = []
    for i in range(len(permu)):
        if find_ban(permu[i], banned_id):     
            user = set(permu[i])
            if user not in find:
                find.append(user)
        
    return len(find)