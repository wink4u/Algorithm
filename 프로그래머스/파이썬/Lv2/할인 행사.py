from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    
    check = []
    for i in range(len(want)):
        cnt = number[i]
        for _ in range(cnt):
            check.append(want[i])
    
    check.sort()
    
    for i in range(len(discount) - 9):
        foods = discount[i : i + 10]
        foods.sort()
        
        if check == foods:
            answer += 1
            
    
    
    return answer