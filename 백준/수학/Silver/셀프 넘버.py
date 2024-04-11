import sys
input = sys.stdin.readline

check = [1 for _ in range(10001)]

for i in range(1, 10001):
    value = str(i)
    _sum = i

    for tmp in value:
        _sum += int(tmp)

    if _sum <= 10000:
        check[_sum] = 0

for i in range(1, len(check)):
    if check[i]:
        print(i)