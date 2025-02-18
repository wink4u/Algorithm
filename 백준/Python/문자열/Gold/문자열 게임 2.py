import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    w = input().strip()
    k = int(input())

    count = [0] * 26
    alpa = [[] for _ in range(26)]

    for i in range(len(w)):
        num = ord(w[i]) - 97
        alpa[num].append(i)
        count[num] += 1

    _min = 1e19
    _max = 0

    for i in range(26):
        if count[i] >= k:
            for j in range(len(alpa[i]) - k + 1):
                _min = min(_min, alpa[i][j + k - 1] - alpa[i][j] + 1)
                _max = max(_max, alpa[i][j + k - 1] - alpa[i][j] + 1)

    if _min == 1e19 and _max == 0:
        print(-1)
    else:
        print(_min, _max)