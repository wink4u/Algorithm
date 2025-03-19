import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
dish = [int(input()) for _ in range(n)]
dish.extend(dish)
answer = 0
dic = defaultdict(int)

left, right = 0, 0
dic[c] = 1

while right < k:
    dic[dish[right]] += 1
    right += 1

while right < len(dish):
    answer = max(answer, len(dic))

    dic[dish[left]] -= 1

    if dic[dish[left]] == 0:
        del dic[dish[left]]

    dic[dish[right]] += 1

    left += 1
    right += 1

print(answer)