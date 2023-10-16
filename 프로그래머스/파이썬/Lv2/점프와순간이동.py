def solution(n):
    # 순간이동은 현재 온 거리 x2
    # 순간이동 건전지 사용량 X, k칸 점프 K 만큼의 건전지 사용량
    ans = 1
    if n == 1:
        return 1
    
    while True:
        if n % 2:
            n -= 1
            ans += 1
        else:
            n /= 2
        
        if n == 1:
            break
        

    return ans