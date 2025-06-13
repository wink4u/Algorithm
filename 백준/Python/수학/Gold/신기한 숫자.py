import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())

if b % a:
    print(0)
else:
    c = b // a
    cnt = 0
    for i in range(1, int(math.sqrt(c)) + 1):
        if c % i == 0:
            if c // i == i:
                cnt += 1
            else:
                cnt += 2

    print(cnt)