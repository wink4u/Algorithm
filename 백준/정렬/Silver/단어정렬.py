import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
word = defaultdict(list)
for _ in range(N):
    tmp = input().strip()

    if tmp not in word[len(tmp)]:
        word[len(tmp)].append(tmp)

dict_word = list(word.items())
dict_word.sort(key = lambda x : (x[0], x[1].sort()))

for i in range(len(dict_word)):
    _, temp = dict_word[i]
    for j in range(len(temp)):
        print(temp[j])