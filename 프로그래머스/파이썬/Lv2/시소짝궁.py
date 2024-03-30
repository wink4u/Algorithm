from collections import Counter
from itertools import combinations, permutations

def solution(weights):
    weight_cnt = Counter(weights)
    dists = [2,3,4]
    combination_list = list(permutations(dists, 2))

    answer = 0

    for key in weight_cnt:
        if weight_cnt[key] > 1 :
            answer += weight_cnt[key] * ( weight_cnt[key] - 1 ) // 2
        for i, j in combination_list:
            expection = key * i / j
            if expection in weight_cnt:
                answer += weight_cnt[key] * weight_cnt[expection]
        weight_cnt[key] = 0

    return answer