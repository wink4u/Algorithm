import sys
import math
input = sys.stdin.readline

a, b, c = map(int, input().split())

flag = 0
first = -b / (2 * a)
sqt = b * b - (4 * a * c)

if sqt < 0:
    flag = 1
elif sqt == 0:
    flag = 2

if flag == 0:
    print(f'{first + (math.sqrt(sqt) / (2 * a)):.2f}')
    print(f'{first - (math.sqrt(sqt) / (2 * a)):.2f}')
elif flag == 1:
    second = math.sqrt(-sqt) / (2 * a)
    if second > 0:
        print(f'{first:.2f}' + '+' + f'{second:.2f}' + 'i')
        print(f'{first:.2f}' + '-' + f'{second:.2f}' + 'i')
    else:
        print(f'{first:.2f}' + '+' + f'{-second:.2f}' + 'i')
        print(f'{first:.2f}' + f'{second:.2f}' + 'i')
else:
    print(f'{first:.2f}')

