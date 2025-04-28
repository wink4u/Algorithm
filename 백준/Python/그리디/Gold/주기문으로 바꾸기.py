import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
s = input().strip()

res = 1e6
for i in range(1, n + 1):
    c = [defaultdict(int) for _ in range(i)]
    for j in range(len(s)):
        c[j % i][s[j]] += 1

    cnt = 0

    for k in range(i):
        lst = list(c[k].values())
        _max = max(lst)
        flag = 0
        for ls in lst:
            if ls == _max:
                if flag:
                    cnt += ls
                else:
                    flag = 1
            else:
                cnt += ls

    res = min(cnt, res)

print(res)