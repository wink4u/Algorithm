import sys
from itertools import combinations
input = sys.stdin.readline

s = list(input().strip())
stack = []
check = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    elif s[i] == ')':
        check.append((stack.pop(), i))

ans = set()

for i in range(len(check)):
    comb = list(combinations(check, i + 1))
    for c in comb:
        tmp = s[:]
        for x, y in c:
            tmp[x] = tmp[y] = ''

        ans.add(''.join(tmp))

ans = list(ans)
ans.sort()

for a in ans:
    print(a)