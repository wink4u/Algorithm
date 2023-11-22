from collections import defaultdict

def solution(topping):
    answer = 0
    
    toppings = defaultdict(int)
    compare = defaultdict(int)
    
    for i in topping:
        toppings[i] += 1
    
    for i in topping:
        toppings[i] -= 1
        compare[i] += 1
        if toppings[i] == 0:
            del toppings[i]
        
        
        if len(toppings) == len(compare):
            answer += 1
    
    return answer