from collections import deque

def solution(s):
    answer = 0
    
    cnt = 0
    q = deque(s)
    
    gwalho_in = ['{', '[', '(']
    gwalho_out = ['}', ']', ')']
    while True:
        stack = []
        flag = 0
        
        for i in range(len(s)):
            if q[i] in gwalho_in:
                stack.append(q[i])
            else:
                if stack:
                    if gwalho_in.index(stack[-1]) == gwalho_out.index(q[i]):
                        stack.pop()
                    else:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
        
        temp = q.popleft()
        q.append(temp)
        
        if flag == 0 and len(stack) == 0:
            answer += 1
                    
        cnt += 1
        if cnt == len(s):
            break
            
    return answer