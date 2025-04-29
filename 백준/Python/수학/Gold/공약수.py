import sys
import math
input = sys.stdin.readline

g, l = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


div = l // g


for a in range(int(math.sqrt(div)), 0, -1):
    b = int(div / a)

    if div % a == 0 and gcd(a, b) == 1:
        print(a * g, b * g)
        break