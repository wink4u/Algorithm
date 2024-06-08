import sys
input = sys.stdin.readline

N, H = map(int, input().split())

obstacle = []
for i in range(N):
    obstacle.append(int(input()))

print(obstacle)