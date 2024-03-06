import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 끊어진 기타줄의 개수, 기타줄 브랜드 수

res = 0

six = []
one = []
for i in range(M):
    a, b = map(int, input().split())
    six.append(a)
    one.append(b)

min_six = min(six)

while N > 0:
    if N >= 6:
        min_one = min(one) * 6
        N -= 6
    else:
        min_one = min(one) * N
        N -= N

    if min_one < min_six:
        res += min_one
    else:
        res += min_six

print(res)