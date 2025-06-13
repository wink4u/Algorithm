import sys
input = sys.stdin.readline

n = int(input())
student = list(map(int, input().split()))
p, q, r, s = map(int, input().split())

start, end = 1, 2 * (10 ** 10)
ans = -1
while start <= end:
    mid = (start + end) // 2

    res = 0
    for i in range(n):
        score = student[i]
        if score > mid + r:
            res += score - p
        elif score < mid:
            res += score + q
        else:
            res += score

    if res < s:
        start = mid + 1
    else:
        end = mid - 1


if start >= 2 * (10 ** 10):
    print(-1)
else:
    print(start)