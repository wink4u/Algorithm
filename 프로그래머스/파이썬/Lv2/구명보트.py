# 효율성 테스트 모두 시간초과
def solution(people, limit):
    
    answer=  0
    
    people.sort()  
    
    visit = [0 for _ in range(len(people))]
    count = 0
    while True:
        if visit[count] or count == len(people) - 1:
            answer += visit.count(0)
            return answer
        
        for i in range(len(people) - 1, count, -1):
            if not visit[i]:
                if people[count] + people[i] <= limit:
                    visit[count], visit[i] = 1, 1
                    answer += 1
                    break
                    
        count += 1
        
        
    return answer

# 효율성 테스트 성공
def solution(people, limit):
    
    answer=  0
    
    people.sort()  


    visit = [0 for _ in range(len(people))]
    count = 0
    while True:
        if visit[count] or count == len(people) - 1:
            answer += visit.count(0)
            return answer
        
        for i in range(len(people) - 1, count, -1):
            if not visit[i]:
                if people[count] + people[i] <= limit:
                    visit[count], visit[i] = 1, 1
                    answer += 1
                    break
                    
        count += 1