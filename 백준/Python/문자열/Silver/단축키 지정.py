import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
dic = defaultdict(bool)

def check(num):
    if num >= 97:
        return chr(num - 32)
    return chr(num)

for _ in range(n):
    s = list(input().split())

    flag = 0
    for i in range(len(s)):
        now = s[i][0]
        od = check(ord(now))
        if dic[od]:
            continue

        dic[od] = True
        s[i] = s[i].replace(now, f'[{now}]', 1)
        flag = 1
        break

    if flag:
        print(' '.join(s))
        continue

    flag2 = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            now = s[i][j]
            od = check(ord(now))
            if dic[od]:
                continue

            dic[od] = True
            s[i] = s[i].replace(now, f'[{now}]', 1)
            flag2 = 1
            break

        if flag2:
            break

    print(' '.join(s))