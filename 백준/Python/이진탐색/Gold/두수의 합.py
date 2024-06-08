import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    num.sort()

    minValue = 1e20
    cnt =1

    for i in range(N):
        L = i + 1
        R = N - 1

        while L <= R:
            mid = (L + R) //2
            _sum = num[i] + num[mid]

            if _sum > K:
                R = mid - 1
            else:
                L = mid + 1

            if abs(K - _sum) < minValue:
                cnt = 1
                minValue = abs(K - _sum)
            elif abs(K - _sum) == minValue:
                cnt += 1

    print(cnt)