from collections import defaultdict

def check(value, N, citations):
    total = 0
    for i in range(N):
        if citations[i] >= value:
            total += 1

    if total >= value:
        return 1
    else:
        return 0

    
def solution(citations):
    answer = 0
    
    # n편중, h번이상 인용된 논문이 h편이상이고 나머지 논문이
    # h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index
    
    citations.sort()
    
    answer = 0
    L = 0
    R = max(citations)
    
    while (L <= R):
        mid = (L + R) // 2

        if (check(mid, len(citations), citations)):
            L = mid + 1
            answer = mid
        else:
            R = mid - 1
    
    return answer