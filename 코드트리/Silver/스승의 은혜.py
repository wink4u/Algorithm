import sys
input = sys.stdin.readline

N, price = map(int, input().split())
gift = []

for _ in range(N):
    a, b = map(int, input().split())
    _sum = a + b
    gift.append([a, _sum])

DP = [[] for _ in range(N)]

res = 0
gift.sort(key = lambda x: (x[1], x[0]))

for i in range(N):
    a, _sum = gift[i]

    if price < _sum:
        if price < _sum - (a / 2):
            break
        else:
            price -= _sum - (a / 2)
            res += 1
    else:
        price -= _sum
        res += 1

print(res)