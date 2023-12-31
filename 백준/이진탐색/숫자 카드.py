import sys
input = sys.stdin.readline

N = int(input())
sang = list(map(int, input().split()))

dic = {}
for i in sang:
    dic[i] = 1

M = int(input())
cards = list(map(int, input().split()))

result = [0 for _ in range(len(cards))]

for i in range(len(cards)):
    if dic.get(cards[i]) == 1:
        result[i] = 1

print(*result)
