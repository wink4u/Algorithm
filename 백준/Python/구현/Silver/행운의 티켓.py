import sys
input = sys.stdin.readline

s = list(map(int, input().strip()))
res = 0
for k in range(1, len(s) // 2 + 1):
    for i in range(len(s)):
        a, b = s[i: i + k], s[i + k: i + 2 * k]
        if len(a) == len(b):
            if sum(a) == sum(b):
                res = max(res, k * 2)
        else:
            break

print(res)