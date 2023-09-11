def solution(s):
    answer = -1
    
    stack = []
    
    for alpha in s:
        if stack:
            temp = stack.pop()
            if temp != alpha:
                stack.append(temp)
                stack.append(alpha)
        else:
            stack.append(alpha)
    
    if stack:
        return 0
    else:
        return 1