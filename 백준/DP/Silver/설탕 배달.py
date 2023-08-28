import sys
input = sys.stdin.readline

N = int(input())
sugar = [5001] * (N + 5)

sugar[3] = sugar[5] = 1

for i in range(6, N + 1):
    sugar[i] = min(sugar[i - 3], sugar[i - 5]) + 1

print(sugar[N] if sugar[N] < 5001 else -1)
