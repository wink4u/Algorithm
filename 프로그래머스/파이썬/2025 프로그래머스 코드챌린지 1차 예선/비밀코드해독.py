from itertools import combinations


def solution(n, q, ans):
    answer = 0

    nums = list(combinations([i for i in range(1, n + 1)], 5))

    for num in nums:
        flag = 0

        for i in range(len(q)):
            cnt = 0
            for j in range(5):
                if q[i][j] in num:
                    cnt += 1
            if cnt != ans[i]:
                flag = 1
                break

        if not flag:
            answer += 1
    return answer