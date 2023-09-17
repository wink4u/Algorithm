import itertools
    
def solution(numbers):
    answer = ''
    if sum(numbers) == 0:
        return '0'
    
    numbers.sort(key = lambda x : (str(x) * 4, str(x) * 3, str(x) * 2, str(x)), reverse = True)
    
    for i in numbers:
        answer += str(i)
            
    return answer