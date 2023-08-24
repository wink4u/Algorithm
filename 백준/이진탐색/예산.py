import sys
input = sys.stdin.readline

# 지방의 수 N
N = int(input())

# 지방 리스트
jibang = list(map(int, input().split()))

budget = int(input())

def check(value):

    total = 0

    for i in range(N):
        if jibang[i] > value:
            total += value
        else:
            total += jibang[i]

    if total <= budget:
        return 1
    else:
        return 0



if sum(jibang) <= budget:
    print(max(jibang))
else:
    L = 0
    R = 1000000000
    ans = 0
    while (L <= R):
        mid = (L + R) // 2
        if check(mid):
            L = mid + 1
            ans = mid
        else:
            R = mid - 1


    print(ans)
