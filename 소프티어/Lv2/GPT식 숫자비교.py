import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
check = defaultdict(list)

for _ in range(n):
    num = input().strip()
    num = num.split('.')
    if len(num) == 1:
        check[num[0]].append(-1)
    else:
        check[num[0]].append(int(num[1]))

c_item = list(check.items())
c_item.sort(key = lambda x : int(x[0]))

for i in range(len(c_item)):
    number = c_item[i][0]
    t = c_item[i][1]
    t.sort()
    for tt in t:
        if tt == -1:
            print(number)
        else:
            print(f'{number}.{tt}')