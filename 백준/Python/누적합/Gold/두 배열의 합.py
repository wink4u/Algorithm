import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

res = 0
C = Counter()

for i in range(N):
    for j in range(i, N):
        C[sum(arr1[i:j+1])] += 1

for i in range(M):
    for j in range(i, M):
        t = T - sum(arr2[i: j+1])
        res += C[t]

print(res)