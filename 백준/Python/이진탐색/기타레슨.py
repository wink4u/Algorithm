import sys

input = sys.stdin.readline

# 강의의 수 N, M
N, M = map(int, input().split())
classes = list(map(int, input().split()))

value = max(classes)
R = sum(classes)
L = value
res = 1000000000

while(L <= R):
    mid = (L + R) // 2

    total = 0
    cnt = 1

    for i in range(N):
        if total + classes[i] > mid:
            cnt += 1
            total = classes[i]
        else:
            total += classes[i]

        if cnt > M:
            break

    if cnt > M:
        L = mid + 1
    else:
        R = mid - 1
        if mid >= value:
            res = min(res, mid)

print(res)