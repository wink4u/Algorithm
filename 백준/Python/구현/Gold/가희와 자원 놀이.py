import sys
input = sys.stdin.readline
from collections import defaultdict

n, t = map(int, input().split())
arr = list(map(int, input().split()))
command = [list(input().split()) for _ in range(t)]
check = defaultdict(int)
cards = defaultdict(tuple)

i = 0
ans = []
for now in arr:
    if cards[now]:
        idx, c, v = cards[now]
        if check[v]:
            cards[now] = (idx, c, v)
        else:
            del cards[now]
            check[v] = 1

        ans.append(idx)
    else:
        com = command[i]
        if com[1] == 'acquire':
            if not check[com[2]]:
                check[com[2]] = 1
            else:
                cards[now] = tuple(com)
        elif com[1] == 'release':
            check[com[2]] = 0

        ans.append(com[0])
        i += 1

print('\n'.join(ans))
