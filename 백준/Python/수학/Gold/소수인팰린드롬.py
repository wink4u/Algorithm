import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())
arr = []

if b > 10000000:
    b = 10000000

for num in range(a, b + 1):
    s_num = str(num)
    if s_num == s_num[::-1]:
        arr.append(num)


def check(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


for a in arr:
    if check(a):
        print(a)

print(-1)
