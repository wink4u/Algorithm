import sys
import math
input = sys.stdin.readline

N = int(input())

def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def check(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(1, 10, 2):
            tmp = num * 10 + i

            if primenumber(tmp) == True:
                check(tmp)

check(2)
check(3)
check(5)
check(7)
