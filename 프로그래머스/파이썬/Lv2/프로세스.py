from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque()
    imp = priorities[location]
    
    for prior in enumerate(priorities):
        q.append(prior)
    
    while True:
        index, value = q.popleft()
        
        for num, val in q:
            if val > value:
                q.append((index, value))
                flag = 1
                break      
        else:
            answer += 1
            if value == imp and index == location:
                return answer