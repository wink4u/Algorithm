import sys
import copy
input = sys.stdin.readline

N = int(input())

word = list(input().strip())
ans = 0

for _ in range(N - 1):
    check = copy.deepcopy(word)
    next_word = input().strip()
    cnt = 0

    for w in next_word:
        if w in check:
            check.remove(w)
        else:
            cnt += 1

    if cnt < 2 and len(check) < 2:
        ans += 1

print(ans)