from collections import defaultdict


def solution(genres, plays):
    answer = []

    check = defaultdict(list)
    _sum = defaultdict(int)

    for i in range(len(genres)):
        genre = genres[i]

        if _sum[genre]:
            _sum[genre] += plays[i]
        else:
            _sum[genre] = plays[i]

        check[genre].append([plays[i], i])

    _sum_item = list(_sum.items())
    _sum_item.sort(key=lambda x: -x[1])

    for g, value in _sum_item:
        g_list = check[g]
        if len(g_list) == 1:
            answer.append(g_list[0][1])
            continue
        g_list.sort(key=lambda x: -x[0])

        for i in range(2):
            answer.append(g_list[i][1])

    return answer