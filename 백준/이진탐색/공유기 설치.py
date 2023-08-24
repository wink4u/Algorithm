import sys
input = sys.stdin.readline

N, C = map(int, input().split())

sensor = []
for i in range(N):
    sensor.append(int(input()))

sensor.sort()

def check(value):
    cnt = 1
    start = sensor[0]

    for i in range(1, N):
        if sensor[i] - start >= value:
            start = sensor[i]
            cnt += 1

    if cnt >= C:
        return 1
    else:
        return 0

L = 0
R = 1000000000
ans = 0

while(L <= R):
    mid = (L + R) // 2
    res = check(mid)
    if res:
        L = mid + 1
        ans = mid
    else:
        R = mid - 1

print(ans)