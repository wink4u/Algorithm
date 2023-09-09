def solution(n):
    DP = [0 for _ in range(n + 1)]
    answer = 0
    DP[0] = 0
    DP[1] = 1
    
    for i in range(2, n + 1):
        DP[i] = (DP[i - 1] + DP[i - 2]) % 1234567

    return DP[n]