import sys
input = sys.stdin.readline

X = input().strip()
cnt = 0

while len(X) != 1:
    _sum = 0

    for x in X:
        _sum += int(x)

    X = str(_sum)
    cnt += 1

print(cnt)
if int(X) % 3:
    print('NO')
else:
    print('YES')