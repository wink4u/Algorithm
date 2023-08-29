import sys
from collections import defaultdict
input = sys.stdin.readline

# 상근이가 가지고 있는 숫자 카드의 개수
N = int(input())

# 숫자 카드에 적혀있는 정수
card = list(map(int, input().split()))
card_dict = defaultdict(int)

for i in card:
    card_dict[i] += 1

# 몇개 가지고 있는지 판단하는 M개의 정수
M = int(input())

# 정답을 넣은 list
res = []
M_card = list(map(int, input().split()))

for i in M_card:
    if card_dict[i]:
        res.append(card_dict[i])
    else:
        res.append(0)

print(*res)

