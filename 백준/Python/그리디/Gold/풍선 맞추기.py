import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arrow = [0] * 1000001

for h in arr:
    if arrow[h] > 0:
        arrow[h] -= 1
        arrow[h - 1] += 1
    else:
        arrow[h - 1] += 1

    print(arrow)

print(sum(arrow))
