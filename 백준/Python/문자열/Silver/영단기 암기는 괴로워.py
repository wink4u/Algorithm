import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
dict = defaultdict(int)

for i in range(N):
    s = input().strip()

    if len(s) >= M:
        dict[s] += 1


dict_value = list(dict.items())
dict_value.sort(key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in range(len(dict_value)):
    print(dict_value[i][0])