import sys
input = sys.stdin.readline

n = int(input())

for r in range(2, int(1e6) + 1):
    total = 1
    now = 1
    check = [1]
    while total < n:
        now *= r
        total += now
        check.append(now)
        if total > n:
            break
        if len(check) >= 3 and n % total == 0:
            a = n // total
            result = [a * t for t in check]
            print(len(result))
            print(*result)
            exit()

print(-1)