from itertools import permutations
import math


def solution(numbers):
    answer = 0

    tmp = []

    def check(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

    for i in range(1, len(numbers) + 1):
        for i in permutations(numbers, i):
            res = int("".join(list(i)))
            if res >= 2 and res not in tmp:
                if check(res):
                    tmp.append(res)

    return len(tmp)