import sys
from collections import defaultdict, Counter
input = sys.stdin.readline

# 정중앙 글자 반드시 사용
# 단어 최소 4글자 이상

dic = []

while True:
    tmp = input().strip()
    if tmp == '-':
        break

    dic.append([len(tmp), Counter(tmp)])

test = []

while True:
    tmp = input().strip()
    if tmp == '#':
        for i in test:
            print(*i)
        break

    # 문자표 딕셔너리
    c_dic = Counter(tmp)
    # 답 확인 딕셔너리
    check = defaultdict(int)

    for t in tmp:
        check[t] = 0

    # item 변환
    c_item = list(c_dic.items())

    for i in range(len(dic)):
        cnt = 0
        s = []
        for j in range(len(c_item)):
            # 퍼즐에 있는 alphabet, 개수
            alp, count = c_item[j]

            if dic[i][1][alp] and dic[i][1][alp] <= count:
                s.append(alp)
                cnt += dic[i][1][alp]

        if cnt == dic[i][0]:
            for k in s:
                check[k] += 1

    check_item = list(check.items())
    check_item.sort(key = lambda x : -x[1])
    _max, _min = check_item[0][1], check_item[-1][1]
    mx_arr, mi_arr = [], []

    for i in range(len(check_item)):
        if check_item[i][1] == _max:
            mx_arr.append(check_item[i][0])
        if check_item[i][1] == _min:
            mi_arr.append(check_item[i][0])

    mi_arr.sort()
    mx_arr.sort()
    test.append([''.join(mi_arr), _min, ''.join(mx_arr), _max])