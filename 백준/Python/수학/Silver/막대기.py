import sys
input = sys.stdin.readline

x = int(input())
count = 0
stick = [64, 32, 16, 8, 4, 2, 1]

for i in range(len(stick)):
    if x >= stick[i]:
        count += 1
        x -= stick[i]

    if x == 0:
        break

print(count)