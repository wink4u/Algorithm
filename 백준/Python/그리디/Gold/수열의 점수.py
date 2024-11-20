import sys
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
zero = []

for i in range(n):
    num = int(input())

    if num < 0:
        minus.append(num)
    elif num > 0:
        plus.append(num)
    else:
        zero.append(num)

minus.sort(reverse = True)
plus.sort()
res = 0

flag1, flag2 = 0, 0
prev= 0

while plus:
    if not flag1:
        prev = plus.pop()
        flag1 = 1
    elif flag1 == 1:
        tmp = plus.pop()
        if tmp == 1:
            res += prev
            res += tmp
            flag1 = 2
        else:
            res += prev * tmp
            flag1 = 0
    else:
        res += plus.pop()

if flag1 == 1:
    res += prev

while minus:
    if not flag2:
        prev = minus.pop()
        flag2 = 1
    else:
        res += prev * minus.pop()
        flag2 = 0

if flag2:
    if zero:
        print(res)
    else:
        print(res + prev)
else:
    print(res)
