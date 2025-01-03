def solution(coin, cards):
    answer = 1
    n = len(cards)
    init = set(cards[:(n // 3)])
    left = cards[n // 3:][::-1]
    pick = set()

    while True:
        if len(left) == 0:
            break

        pick.add(left.pop())
        pick.add(left.pop())
        is_pick = False

        for i in list(init):
            other = n + 1 - i

            if other in init and i != other:
                init.remove(i)
                init.remove(other)

                answer += 1
                is_pick = True
                break

        if is_pick:
            continue

        if coin >= 1 and init and pick:
            for i in list(init):
                other = n + 1 - i

                if other in pick:
                    init.remove(i)
                    pick.remove(other)

                    answer += 1
                    is_pick = True
                    coin -= 1
                    break

        if is_pick:
            continue

        if coin >= 2 and pick:
            for i in list(pick):
                other = n + 1 - i
                if other in pick:
                    pick.remove(other)
                    pick.remove(i)

                    answer += 1
                    is_pick = True
                    coin -= 2
                    break

        if is_pick:
            continue

        break

    return answer