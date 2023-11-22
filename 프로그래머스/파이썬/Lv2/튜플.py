def solution(s):
    answer = []
    
    temp = []
    check_s = []
    str_s = ''
    flag = 0
    for check in s:
        if check.isdigit():
            str_s += check
        elif check == ',':
            if flag == 1:
                temp.append(str_s)
                str_s = ''
        elif check == '{':
            flag = 1
        elif check == '}':
            if temp:
                temp.append(str_s)
                check_s.append(temp)
                temp = []
                str_s = ''
            else:
                if str_s:
                    check_s.append([str_s])
                    str_s = ''
            flag = 0
            
    check_s.sort(key = lambda x : len(x))
    
    answer.append(int(check_s[0][0]))
    
    for i in range(1, len(check_s)):
        
        for res in check_s[i]:
            if int(res) not in answer:
                answer.append(int(res))
                break
                
    return answer