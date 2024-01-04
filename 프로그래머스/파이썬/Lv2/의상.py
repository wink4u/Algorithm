from collections import defaultdict

def solution(clothes):
    # 하나의 의상에 안 입을 경우를 추가해서
    # 모든 경우의수를 다 곱한후
    # 안입을 경우 값을 -1 해줘서 구함
    answer = 1
    
    wears = defaultdict(int)
    
    for cloth, wear in clothes:
        wears[wear] += 1
    
    for i in wears.values():
        answer *= i + 1
        
    return answer - 1