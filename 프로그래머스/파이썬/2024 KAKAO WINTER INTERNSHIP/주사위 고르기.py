from itertools import combinations
from collections import defaultdict


def solution(dice):
    answer = []
    _max = 0
    check = []

    if len(dice) > 2:
        d_list = [i for i in range(1, len(dice) + 1)]
        com = list(combinations(d_list, len(dice) // 2))
        a_dice = com[:len(com) // 2]
        b_dice = []

        n = len(a_dice)
        total = 6 ** ((len(dice) // 2) ** 2)

        for i in range(n):
            tmp = []
            for j in range(len(d_list)):
                if d_list[j] not in a_dice[i]:
                    tmp.append(d_list[j])

            b_dice.append(tmp)

        for i in range(n):
            a = a_dice[i]
            b = b_dice[i]

            ares = defaultdict(int)
            bres = defaultdict(int)

            def aroll(dice, select, now, arr):
                if len(arr) == len(select):
                    _sum = sum(arr)
                    ares[_sum] += 1
                    return

                for i in range(6):
                    arr.append(dice[select[now] - 1][i])
                    aroll(dice, select, now + 1, arr)
                    arr.pop()

            def broll(dice, select, now, arr):
                if len(arr) == len(select):
                    _sum = sum(arr)
                    bres[_sum] += 1
                    return

                for i in range(6):
                    arr.append(dice[select[now] - 1][i])
                    broll(dice, select, now + 1, arr)
                    arr.pop()

            aroll(dice, a, 0, [])
            broll(dice, b, 0, [])

            aroll_list = list(ares.items())
            broll_list = list(bres.items())

            win, lose = 0, 0

            for j in range(len(aroll_list)):
                for k in range(len(broll_list)):
                    if aroll_list[j][0] > broll_list[k][0]:
                        win += aroll_list[j][1] * broll_list[k][1]
                    elif aroll_list[j][0] < broll_list[k][0]:
                        lose += aroll_list[j][1] * broll_list[k][1]

            check.append([win, a])
            check.append([lose, b])

        check.sort(key=lambda x: -x[0])

        return list(check[0][1])
    else:
        ar, br = 0, 0
        for i in range(6):
            a = dice[0][i]
            for j in range(6):
                b = dice[1][j]

                if a > b:
                    ar += 1
                elif a < b:
                    br += 1

        if ar > br:
            return [1]
        else:
            return [2]

