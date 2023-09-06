import heapq

def solution(operations):
    
    max_q = []
    min_q = []
    # command가 D고 number이 1 일때 최댓값 삭제
    # coomand가 D가 number이 -1 일때 최솟값 삭제
    
    max_cnt = 0
    min_cnt = 0
    for i in range(len(operations)):
        command,number = operations[i].split()
        
        number = int(number)
        
        if command == 'I':
            heapq.heappush(max_q, -number)
            heapq.heappush(min_q, number)
        
        elif command == 'D':
            if max_q and min_q:
                if number == 1:
                    res = heapq.heappop(max_q)
                    min_q.remove(-res)
                else:
                    res = heapq.heappop(min_q)
                    max_q.remove(-res)
    
    if max_q:
        answer = [-heapq.heappop(max_q), heapq.heappop(min_q)]
    else:
        answer = [0, 0]
    return answer