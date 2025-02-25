def solution(players, m, k):
    answer = 0
    check = [0] * 24

    def cal(num):
        if num < m:
            return 0
        v = num // m
        return v

    for i in range(24):
        p = players[i]

        cnt = cal(p)
        if cnt:
            if check[i] < cnt:
                value = cnt - check[i]
                answer += value
                for j in range(i, min(i + k, 24)):
                    check[j] += value

    return answer