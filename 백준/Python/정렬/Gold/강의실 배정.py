import sys
import heapq
input = sys.stdin.readline

N = int(input())
classes = []
for _ in range(N):
    classes.append(list(map(int, input().split())))

classes.sort(key = lambda x : (x[0], x[1]))

check = []
heapq.heappush(check, classes[0][1])

for i in range(1, N):
    if check[0] > classes[i][0]:
        heapq.heappush(check, classes[i][1])
    else:
        heapq.heappop(check)
        heapq.heappush(check, classes[i][1])

print(len(check))