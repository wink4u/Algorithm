import sys
input = sys.stdin.readline

n, b, w = map(int, input().split())
arr = list(input().strip())
check = {'W': 0, 'B': 1}

l = 0
wb = [0, 0]
answer = 0
for r in range(n):
    wb[check[arr[r]]] += 1

    while wb[1] > b:
       wb[check[arr[l]]] -= 1
       l += 1

    if wb[0] >= w:
        answer = max(answer, r - l + 1)

print(answer)