def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    for i in range(row_begin - 1, row_end):
        res = 0
        for da in data[i]:
            res += da % (i + 1)

        answer ^= res
    return answer