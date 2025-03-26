import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

arr.sort(reverse=True)
box.sort(reverse=True)

if arr[0] < box[0]:
    print(-1)
else:
    cnt = 0

    while box:
        cnt += 1

        for w in arr:
            if len(box) == 0:
                break

            elif w < box[-1]:
                break

            for b in box:
                if b <= w:
                    box.remove(b)
                    break

    print(cnt)