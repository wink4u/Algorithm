import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = [0] * 4
for i in range(n):
    cnt[arr[i]] += 1
s = set()
score = []
for i in range(4):
    for j in range(4):
        tmp = [i, j]
        tmp.sort()

        if tuple(tmp) not in s:
            s.add(tuple(tmp))
            score.append((tmp, i ^ j))

score.sort(key = lambda x : (-x[1]))
res = 0
for i in range(len(score)):
    f, s = score[i][0]

    if cnt[f] and cnt[s]:
        c = min(cnt[f], cnt[s])
        cnt[f] -= c
        cnt[s] -= c
        res += c * score[i][1]

print(res)