import sys
from collections import defaultdict
input = sys.stdin.readline

alphas = input().strip()

alpha_dict = defaultdict(int)

total = len(alphas)

for alpha in alphas:
    alpha_dict[alpha] += 1

sorted_dict = dict(sorted(alpha_dict.items()))

odd = 0
flag = 0
res = ''
center = ''
for i, cnt in sorted_dict.items():
    if cnt % 2:
        odd += 1
        center = i
        if odd > 1:
            flag = 1
            break

    plus = 0
    if cnt == 1:
        continue

    while True:
        res += i
        plus += 1

        if plus == cnt // 2:
            break

if flag:
    print("I'm Sorry Hansoo")
else:
    reverse_res = sorted(res, reverse=True)
    temp = ''
    for i in reverse_res:
        temp += i
    print(res + center + temp)