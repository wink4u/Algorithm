import sys
from math import comb
input = sys.stdin.readline

a = int(input())
b = int(input())

a_goal, a_no = a / 100, (100 - a) / 100
b_goal, b_no = b / 100, (100 - b) / 100

check = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]

res_a = 0
res_b = 0

for k in check:
    res_a += comb(18, k) * (a_goal ** k) * (a_no ** (18 - k))
    res_b += comb(18, k) * (b_goal ** k) * (b_no ** (18 - k))

print(1 - (res_a * res_b))