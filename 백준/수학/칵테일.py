import sys
from collections import deque
input = sys.stdin.readline

# N 재료의 개수
N = int(input())

# 최대공약수 함수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

line = [0 for _ in range(N)]
sa, sb, p, q = map(int, input().split())
di = gcd(p, q)
line[sa] = p // di
line[sb] = q // di
first = [sa, sb]

temp = deque()
start = [0 for _ in range(N)]
start[sa] = start[sb] = 1
for i in range(N - 2):
    a, b, p, q = map(int, input().split())
    di = gcd(p, q)

    if a in first:
        for i in range(N):
            if i != a and line[i] >= 1:
                line[i] *= p // di

        line[b] = (line[a] * (q // di))
        line[a] *= p // di
        start[a] += 1
        start[b] += 1

    elif b in first:
        for i in range(N):
            if i != b and line[i] >= 1:
                line[i] *= q // di

        line[a] = (line[b] * (p // di))
        line[b] *= q // di
        start[a] += 1
        start[b] += 1
    else:
        temp.append((a, b, p, q))

if temp:
    while temp:
        for i in range(len(temp)):
            a, b, p, q = temp.popleft()
            di = gcd(p, q)

            if start[a]:
                for i in range(N):
                    if i != a and line[i] >= 1:
                        line[i] *= p // di

                line[b] = (line[a] * (q // di))
                line[a] *= p // di
                start[a] += 1
                start[b] += 1

            elif start[b]:
                for i in range(N):
                    if i != b and line[i] >= 1:
                        line[i] *= q // di

                line[a] = (line[b] * (p // di))
                line[b] *= q // di
                start[a] += 1
                start[b] += 1

            else:
                temp.append((a, b, p, q))

min_value = min(line)
div = 2
while True:
    division = True
    for k in line:
        if k % div == 0:
            continue
        else:
            division = False
            break

    if division == True:
        for j in range(N):
            line[j] = line[j] // div
    else:
        div += 1

    if div > min_value:
        break

print(*line)