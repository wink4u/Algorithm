import sys
input = sys.stdin.readline

N, S = map(int, input().split())

nums = [S] + list(map(int, input().split()))

nums.sort()

temp = []
for i in range(1, len(nums)):
    temp.append(nums[i] - nums[i - 1])

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

res = temp[0]
for i in range(1, len(temp)):
    res = gcd(temp[i], res)

print(res)