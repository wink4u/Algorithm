import math


def solution(k, d):
    answer = 0

    for i in range(0, d + 1, k):
        x = d ** 2 - i ** 2
        cnt = int(x ** (0.5)) // k + 1
        answer += cnt

    return answer