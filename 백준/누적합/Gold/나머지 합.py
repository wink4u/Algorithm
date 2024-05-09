import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
_sum = 0
remainder = [0] * M

for i in range(N):
    _sum += num[i]
    remainder[_sum % M] += 1

result = remainder[0]

for i in remainder:
    result += i * (i - 1) // 2

print(result)