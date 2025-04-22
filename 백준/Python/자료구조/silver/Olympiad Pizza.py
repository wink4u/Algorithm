import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
ans = [0] * n

arr = list(map(int, input().split()))
test = list(enumerate(arr))

q = deque(test)
time = 1
while q:
    index, value = q.popleft()
    ans[index] = time
    time += 1
    value -= 1

    if value:
        q.append((index, value))

print(*ans)