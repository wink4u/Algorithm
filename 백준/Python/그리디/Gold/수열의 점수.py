import sys
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
zero = False

for i in range(n):
    num = int(input())

    if num < 0:
        minus.append(num)
    elif num > 0:
        plus.append(num)
    else:
        zero = True

minus.sort(reverse = True)
plus.sort()
res = 0

flag1, flag2 = 0, 0
prev= 0

while len(plus) > 1:
    a, b = plus.pop(), plus.pop()
    res += a * b if a > 1 and b > 1 else a + b

if plus:
    res += plus[0]

while len(minus) > 1:
    res += minus.pop() * minus.pop()

if minus:
    if not zero:
        res += minus[0]

print(res)