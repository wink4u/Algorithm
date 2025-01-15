import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

zero, one = [], []
res = 0

prev = 1001
while arr:
    now = arr.pop()
    if now > 0:
        if now == 1:
            one.append(now)
        else:
            if prev == 1001:
                prev = now
            else:
                res += prev * now
                prev = 1001
    elif now == 0:
        zero.append(now)
    else:
        arr.append(now)
        break

plus = 0
if prev != 1001:
    res += prev

prev = 1001
arr.sort(reverse = True)

while arr:
    now = arr.pop()
    if prev == 1001:
        prev = now
    else:
        res += prev * now
        prev = 1001

res += len(one)

if prev != 1001 and len(zero) == 0:
    res += prev

print(res)
