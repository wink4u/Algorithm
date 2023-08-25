import sys
input = sys.stdin.readline

# N일 동알 사용할 금액,
N, M = map(int, input().split())

bank = list(int(input()) for _ in range(N))

L = min(bank)
R = 1000000000

def check(value):
    cnt = 1
    money = value

    for i in range(N):
        if bank[i] > money:
            cnt += 1
            money = value
        money -= bank[i]

    if cnt > M or value < max(bank):
        return 1
    else:
        return 0

ans = 0
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        L = mid + 1
    else:
        R = mid - 1
        ans = mid


print(ans)
