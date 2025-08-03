import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
problem = []
level = defaultdict(list)
check = defaultdict(int)

for _ in range(n):
    num, lvl = map(int, input().split())
    check[num] = lvl
    level[lvl].append(num)
    problem.append(lvl)

m = int(input())

for _ in range(m):
    command = list(input().split())

    if command[0] == 'add':
        num, lvl = int(command[1]), int(command[2])
        level[lvl].append(num)
        check[num] = lvl
        if level not in problem:
            problem.append(lvl)
    elif command[0] == 'solved':
        num = int(command[1])
        lvl = check[num]
        idx = level[lvl].index(num)
        level[lvl].pop(idx)

        if len(level[lvl]) == 0:
            del level[lvl]
            p_idx = problem.index(lvl)
            problem.pop(p_idx)

    elif command[0] == 'recommend':
        x = int(command[1])
        if x == 1:
            lvl = max(problem)
            print(max(level[lvl]))
        else:
            lvl = min(problem)
            print(min(level[lvl]))
