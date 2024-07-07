import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = [3 * 60, 3 * 60, 18 * 60]

today = N * 24 * 60
tomorrow = (N + 1) * 24 * 60
minute = 15 * 60

cnt = 0
check = []
while minute < tomorrow:
    if minute >= today:
        check.append(minute)

    minute += arr[cnt % 3]

    if cnt % 3 == 2:
        minute += K
    cnt += 1

def change(num):
    return f'{num // 60 % 24:02}:{num % 60:02}'

print(len(check))
for i in range(len(check)):
    print(change(check[i]))