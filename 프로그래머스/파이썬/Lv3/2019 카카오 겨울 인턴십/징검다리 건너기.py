def solution(stones, k):
    answer = 0
    
    s_stones = list(set(stones))
    s_stones.sort()
    
    L, R = 0, len(s_stones) - 1
    
    while L <= R:
        mid = (L + R) // 2
        if check(s_stones[mid], stones, k):
            L = mid + 1
            answer = s_stones[mid]
        else:
            R = mid - 1
    
    return answer


def check(l, st, k):
    cnt = 0
    for i in range(len(st)):
        if st[i] < l:
            cnt += 1
            if cnt == k:
                return False
        else:
            cnt = 0
    
    return True