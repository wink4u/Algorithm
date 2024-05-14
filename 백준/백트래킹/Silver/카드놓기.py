import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
k = int(input())

arr = [input().strip() for _ in range(n)]

print(len(set("".join(i) for i in permutations(arr, k))))

