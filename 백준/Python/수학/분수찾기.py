import sys
input = sys.stdin.readline

start = 1
value = int(input())
while True:
    if value - start <= 0:
        break
    else:
        value -= start
        start += 1


_sum = start + 1

if _sum % 2:
    print(f'{value}/{_sum - value}')
else:
    print(f'{_sum - value}/{value}')