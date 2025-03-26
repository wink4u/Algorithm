import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    k = m // 10

    for _ in range(k):
        arr.extend(list(map(int, input().split())))

    left = []
    right = []
    res = []
    mid = 0

    for i in range(0, m, 2):
        if i == 0:
            res.append(arr[i])
            mid = arr[i]
        else:
            one = arr[i]
            two = arr[i - 1]

            if mid <= one:
                heapq.heappush(right, one)
            else:
                heapq.heappush(left, -one)

            if mid <= two:
                heapq.heappush(right, two)
            else:
                heapq.heappush(left, -two)

            if len(right) > len(left):
                r = heapq.heappop(right)
                heapq.heappush(left, -mid)
                mid = r
            elif len(left) > len(right):
                l = heapq.heappop(left)
                heapq.heappush(right, mid)
                mid = -l

            res.append(mid)

    res_len = len(res)
    rk = res_len // 10

    print(res_len)
    for i in range(rk + 1):
        print(*res[i * 10: i * 10 + 10])