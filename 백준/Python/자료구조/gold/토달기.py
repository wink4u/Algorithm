import sys
from collections import deque, defaultdict
input = sys.stdin.readline

d, s = input().split()
d = int(d)

def check(prev, nxt):
    if len(nxt) - len(prev) != 1:
        return False

    pi, ni = 0, 0
    flag = 0

    while pi < len(prev) and ni < len(nxt):
        if prev[pi] == nxt[ni]:
            pi += 1
            ni += 1
        else:
            if flag:
                return False
            flag = 1
            ni += 1

    return True


word = [[] for _ in range(81)]
res = s

for _ in range(d):
    ss = input().strip()
    word[len(ss)].append(ss)

q = deque()
q.append(s)
cc = set()

while q:
    now = q.popleft()

    for nxt in word[len(now) + 1]:
        if nxt in cc:
            continue

        if check(now, nxt):
            cc.add(nxt)
            q.append(nxt)
            res = nxt

print(res)