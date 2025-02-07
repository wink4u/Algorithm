import sys
from collections import defaultdict
input = sys.stdin.readline

b = int(input())
low = defaultdict(list)
high = defaultdict(list)

l_c = set()
h_c = set()

for _ in range(b):
    tmp = input().strip()
    l_tmp = len(tmp)

    l_c.add(l_tmp)
    low[l_tmp].append(tmp)

for _ in range(b):
    tmp = input().strip()
    h_tmp = len(tmp)

    h_c.add(h_tmp)
    high[h_tmp].append(tmp)

n = int(input())

l_c, h_c = list(l_c), list(h_c)

for _ in range(n):
    check = input().strip()

    h_cnt, l_cnt = 0, 0
    length = len(check)

    v = [0] * 51

    for i in l_c:
        idx = 0
        flag = 0

        if i in h_c:
            v[i] = 1
            flag = 1

        while idx < i:
            for k in range(idx, length, i):
                c = check[k:k+i]
                if len(c) == i:
                    if c in low[i]:
                        l_cnt += 1

                    if flag:
                        if c in high[i]:
                            h_cnt += 1

            idx += 1

    for i in h_c:
        if v[i]:
            continue

        idx = 0

        while idx < i:
            for k in range(idx, length, i):
                c = check[k:k + i]
                if len(c) == i:
                    if c in high[i]:
                        h_cnt += 1

            idx += 1

    res = h_cnt - l_cnt
    if res > 0:
        print(f'LOW {res}')
    elif res < 0:
        print(f'HIGH {abs(res)}')
    else:
        print('GOOD')