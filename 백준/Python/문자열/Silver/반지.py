import sys
input = sys.stdin.readline

s = input().strip()
l = len(s)
n = int(input())
ans = 0
for i in range(n):
    tmp = input().strip()
    tmp += tmp[:l]
    for j in range(len(tmp) - l):
        if s == tmp[j:j+l]:
            ans += 1
            break


print(ans)