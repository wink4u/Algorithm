def solution(s):
    answer = ''
    
    prev = ' '
    for i in s:
        if prev == ' ':
            if 97 <= ord(i) <= 122:
                answer += chr(ord(i) - 32)
            else:
                answer += i
        else:
            if 65 <= ord(i) <= 90:    
                answer += chr(ord(i) + 32)
            else:
                answer += i
        
        prev = i
        
    return answer