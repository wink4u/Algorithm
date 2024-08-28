import sys
from collections import deque
input = sys.stdin.readline

S, P = map(int, input().split())
DNA = input().strip()
A, C, G, T = map(int, input().split())

l, r = 0, P - 1
dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
q = deque(DNA[l:r])

for i in q:
    dic[i] += 1

res = 0

while r < S:
    dic[DNA[r]] += 1

    if dic['A'] >= A and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T:
        res += 1

    dic[DNA[l]] -= 1
    l += 1
    r += 1

print(res)