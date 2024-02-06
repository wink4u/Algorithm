import sys
import math
input = sys.stdin.readline

N = int(input())
houses = list(map(int, input().split()))

# 소수 판별
def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
        	return False
    return True

_max = 0
for i in range(2, 100):
    if primenumber(i):
        cnt = 0
        for house in houses:
            if house % i == 0:
                cnt += 1
        _max = max(cnt, _max)

print(_max)