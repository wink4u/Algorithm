def solution(phone_book):
    answer = True
    hash = {}
    
    for i in phone_book:
        hash[i] = 1
    
    for phone_num in phone_book:
        temp = ''
        for num in phone_num:
            temp += num
            if temp in hash and temp != phone_num:
                answer = False
                break
                
    return answer