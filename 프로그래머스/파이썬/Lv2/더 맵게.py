import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if len(scoville) == 1:
            if scoville[0] >= K:
                return answer
            else:
                return -1
        
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        
        second = heapq.heappop(scoville)
        
        res = first + (second * 2)
        heapq.heappush(scoville, res)
        answer += 1
        
        
    
    return answer