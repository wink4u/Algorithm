import sys
input = sys.stdin.readline

N, M = map(int, input().split())
book = list(map(int, input().split()))
p, m = [], []
mx = 0
for i in range(N):
    mx = max(mx, abs(book[i]))
    if book[i] > 0:
        p.append(book[i])
    else:
        m.append(book[i])

p.sort(reverse= True)
m.sort()
p += [0]
m += [0]

cnt = 0
now = 0
res = 0

for i in range(len(p)):
    if cnt == 0:
        now = p[i]
    cnt += 1

    if cnt == M or p[i] == 0:
        res += now * 2
        cnt = 0

now = 0
for i in range(len(m)):
    if cnt == 0:
        now = -m[i]
    cnt += 1

    if cnt == M or m[i] == 0:
        res += now * 2
        cnt = 0

print(res - mx)