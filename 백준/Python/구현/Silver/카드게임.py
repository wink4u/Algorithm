import sys
from collections import defaultdict
input = sys.stdin.readline

color = defaultdict(list)
number = defaultdict(int)

for _ in range(5):
    c, n = input().split()

    color[c].append(int(n))
    number[int(n)] += 1

color_items = list(color.items())
number_items = list(number.items())

number_items.sort(key = lambda x : (-x[1], -x[0]))

if len(color_items) == 1:
    max_num = max(color_items[0][1])
    min_num = min(color_items[0][1])

    if max_num - min_num == 4:
        print(900 + max_num)
    else:
        print(600 + max_num)
else:
    max_num = number_items[0][0]
    if len(number_items) == 2:
        if number_items[0][1] == 4:
            print(800 + max_num)
        else:
            print(700 + (10 * max_num) + number_items[1][0])
    elif len(number_items) == 5:
        min_num = int(number_items[4][0])

        if max_num - min_num == 4:
            print(500 + max_num)
        else:
            print(100 + max_num)
    elif len(number_items) == 3:
        if number_items[0][1] == 3:
            print(400 + max_num)
        elif number_items[0][1] == 2:
            print(300 + (10 * max_num) + number_items[1][0])
    elif len(number_items) == 4:
        print(200 + max_num)