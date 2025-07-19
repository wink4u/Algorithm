import sys
from collections import defaultdict
input = sys.stdin.readline

check = defaultdict(set)
count = defaultdict(int)
words = set()
for line in sys.stdin:
    word = line.strip()
    if not word:
        break
    tmp = sorted(list(word))
    s_tmp = ''.join(tmp)
    words.add(s_tmp)
    check[s_tmp].add(word)
    count[s_tmp] += 1


results = []
for word in words:
    fix = list(check[word])
    fix.sort()

    results.append((count[word], fix[0], fix))


results.sort(key = lambda x : (-x[0], x[1]))
cnt = 0
for result in results:
    cnt += 1
    print(f'Group of size {result[0]}: ', end='')
    print(*result[2], end='')
    print(' .')

    if cnt == 5:
        break