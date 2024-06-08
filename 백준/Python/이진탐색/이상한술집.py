import sys
import math

input = sys.stdin.readline

# 주전자의 개수 N, 친구들의 수 K

N, K = map(int, input().split())

bowl = list(int(input()) for _ in range(N))

def check(value):
    cnt = 0

    for i in range(len(bowl)):
        cnt += bowl[i] // value


    if cnt >= K:
        return 1
    else:
        return 0

L = 0
R = math.pow(2, 31) - 1
ans = 0
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        L = mid + 1
        ans = mid
    else:
        R = mid - 1

print(round(ans))





