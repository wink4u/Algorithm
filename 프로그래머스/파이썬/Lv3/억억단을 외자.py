def solution(e, starts):
    answer = []
    check = [0] * (e + 1)
    for i in range(1, e + 1):
        if i * i < e + 1:
            check[i * i] += 1
        for j in range(i + 1, e + 1):
            n = i * j
            if n > e:  # 맨끝수 : e
                break
            check[n] += 2

    dp = [0] * (e + 1)
    _max = 0
    for i in range(e, 0, -1):
        if _max <= check[i]:
            _max = check[i]
            dp[i] = i
        else:
            dp[i] = dp[i + 1]

    for i in starts:
        answer.append(dp[i])

    return answer