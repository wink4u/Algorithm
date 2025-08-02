import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
test = [int(input()) for _ in range(n)]
num = [0] * 1299710
num[0] = 1

for i in range(1, 1299710):
    flag = 0
    for k in range(2, int(i ** 0.5) + 1):
        if i % k == 0:
            flag = 1
            break

    if not flag:
        num[i] = 1


for t in test:
    if num[t]:
        print(0)
    else:
        cnt = 1

        left = t - 1
        right = t + 1

        while True:
            if num[left]:
                break

            cnt += 1
            left -= 1

        while True:
            if num[right]:
                break

            cnt += 1
            right += 1

        print(cnt + 1)