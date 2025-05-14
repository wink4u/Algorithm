import sys
from collections import defaultdict
input = sys.stdin.readline

a = input().strip()
s = input().strip()
n = len(a)

dic = defaultdict(int)

for i in range(n):
    dic[a[i]] = i + 1

res = 0
mod = 900528

for i in range(len(s)):
    c = s[i]
    res = (res * n + dic[c]) % mod

print(res)