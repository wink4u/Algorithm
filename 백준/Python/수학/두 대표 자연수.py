import sys
import math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
res = [0, 0]
res[0] = arr[n // 2] if n % 2 else arr[(n // 2) - 1]

_sum = sum(arr)
cal = _sum / n

res[1] = math.floor(cal) if cal - (_sum // n) <= 0.5 else round(cal)

print(*res)