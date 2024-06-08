import sys
import math
input = sys.stdin.readline

# K 랜선의 개수, N 필요한 랜선의 개수

K, N = map(int, input().split())

line = []
for i in range(K):
    line.append(int(input()))


def check(value):
    total = 0

    for i in range(K):
        total += line[i] // value

    if total >= N:
        return 1
    else:
        return 0

L = 0
R = math.pow(2, 31) - 1

answer = 0

while L <= R:
    mid = (L + R) // 2
    if check(mid):
        L = mid + 1
        answer = mid
    else:
        R = mid - 1

print(round(answer))